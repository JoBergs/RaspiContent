#!/usr/bin/env python
 
import os, sys, time, argparse

import email
from imapclient import IMAPClient

# credentials could be stored here permanently, but that's bad security.
HOSTNAME = 'HOST'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
MESSAGE_SUBJECT = 'TheSubject'

MAILBOX = 'Inbox'
TARGET = '/home/pi/'  # this is the path where attachments are stored 
CHECK_FREQ = 30 # in seconds

def parse_arguments(sysargs):
    """ Setup the command line options. """

    description = '''The script parseIMAPemail.py is looped and repeatedly 
    checks a mail box if a mail with a specified subject has arrived.
    If so, the emails attachment is stored. This script is a part of the tutorial 
    www.knight-of-pi.org/accessing-and-parsing-emails-with-the-raspberry-pi-and-imapclient'''

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u', '--username', nargs='?', metavar='str', type=str,
                                    default=USERNAME, help='Username of the Email account',)
    parser.add_argument('-s', '--subject', nargs='?', metavar='str', type=str,
                                     default=MESSAGE_SUBJECT, help='The subject new emails should be scanned for')
    parser.add_argument('--host', nargs='?', metavar='str', type=str,
                                     default=HOSTNAME, help='Name of the IMAP host webserver')
    parser.add_argument('--pwd', nargs='?', metavar='str', type=str,
                                     default=PASSWORD, help='Password belonging to the username')

    return parser.parse_args(sysargs)

def store_attachment(part):
    """ Store attached files as they are and with the same name. """

    filename = part.get_filename()
    att_path = os.path.join(TARGET, filename)

    if not os.path.isfile(att_path) :
        fp = open(att_path, 'wb')
        fp.write(part.get_payload(decode=True))
        fp.close()
    print "Successfully stored attachment!"

def check_attachment(mail):
    """ Examine if the email has the requested subject and store the attachment if so. """

    print "["+mail["From"]+"] :" + mail["Subject"]

    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        store_attachment(part)
        time.sleep(3)

def scan_emails(args, unread):
    """ Scan all unread Emails for the given Subject. """

    for msg_id, stuff in unread.iteritems():
        new_email = email.message_from_string(unread[msg_id]['RFC822'])
        
        if new_email['subject'] == args.subject:
            print "Found subject! Storing the attachment of mail id ",  msg_id
            check_attachment(new_email)

def loop(args):
    """ Main loop: log into the IMAP server and fetch all unread emails,
         which are delegated into scan_emails. """

    print('Logging into ' + args.username)

    server = IMAPClient(args.host, use_uid=True, ssl=True)
    server.login(args.username, args.pwd)   
    
    select_info = server.select_folder(MAILBOX)
    messages = server.search(['UNSEEN'])
    all_unread = server.fetch(messages, ['RFC822'])
    scan_emails(args, all_unread)

    time.sleep(CHECK_FREQ)


 
if __name__ == '__main__':
    args = parse_arguments(sys.argv[1:])

    try:
        while True:
            loop(args)
    finally:
        pass