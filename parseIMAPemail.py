#!/usr/bin/env python
 
from imapclient import IMAPClient
import email
import time
import os
 
DEBUG = True

HOSTNAME = 'HOST'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
MAILBOX = 'Inbox'

MESSAGE_SUBJECT = 'TheSubject'
 
CHECK_FREQ = 30 # in seconds, as param, too

# make this a parameter, too
target_dir = '/home/pi/'

# add CML parameters for h = help, host, u = username, t = target, pwd and m = mailbox, s = subject

# just save the images with their names,
# expect non-equally named images(or is there a module generate_path or similar???)
def store_attachment(part):
    """ Store attached files as they are and with the same name. """

    filename = part.get_filename()
    att_path = os.path.join(target_dir, filename)

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
 
def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
 
    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    messages = server.search(['UNSEEN'])
    all_unread = server.fetch(messages, ['RFC822'])
    print 'num unread: ', len(all_unread)
    for msg_id, stuff in all_unread.iteritems():
        new_email = email.message_from_string(all_unread[msg_id]['RFC822'])
        print msg_id
        if new_email['subject'] == MESSAGE_SUBJECT:
            print "Storing the attachment"
            check_attachment(new_email)
 
    time.sleep(CHECK_FREQ)
 
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        print 'leaving'