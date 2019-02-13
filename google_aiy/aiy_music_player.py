#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/a-voice-controlled-boombox-with-the-google-aiy-voice-hat/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import logging, os, platform, subprocess, sys, time

from google.assistant.library.event import EventType

from aiy.assistant import auth_helpers
from aiy.assistant.library import Assistant
from aiy.board import Board, Led
import aiy.voice.tts


def power_off_pi():
    aiy.voice.tts.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.voice.tts.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


playshell = None

def play(say):
        track = say.split('play')[-1]

        global playshell
        if (playshell == None):
            playshell = subprocess.Popen(["/usr/local/bin/mpsyt",""], stdin=subprocess.PIPE)

        playshell.stdin.write(bytes('/' + track + '\n1\n', 'utf-8'))
        playshell.stdin.flush()


def process_event(led, event):
    logging.info(event)

    if event.type == EventType.ON_START_FINISHED:
        led.state = Led.BEACON_DARK  # Ready.
        logging.info('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        led.state = Led.ON  # Listening.

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        led.state = Led.PULSE_QUICK  # Thinking.

    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        led.state = Led.BEACON_DARK

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            power_off_pi()
        elif text == 'reboot':
            reboot_pi()
        elif 'play' in text:
            play(text)
        elif 'stop' in text:
            pkill = subprocess.Popen(["/usr/bin/pkill","vlc"],stdin=subprocess.PIPE)


def main():
    logging.basicConfig(level=logging.INFO)

    credentials = auth_helpers.get_assistant_credentials()
    with Board() as board, Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(board.led, event)


if __name__ == '__main__':
    main()
