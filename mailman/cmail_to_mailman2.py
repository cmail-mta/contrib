#!/usr/bin/env python3
#FIXME this is problematic with non-prefix-free list names
import sqlite3
import subprocess
MAILMAN = "/var/lib/mailman/mail/mailman"
DATABASE = "/etc/cmail/databases/master.db3"
USER = 'mailman'
LISTS = [ "devel", "security", "announce" ]

handlers = {    "":"post", 
                "-admin":"admin", 
                "-bounces":"bounces",
                "-confirm":"confirm",
                "-join":"join",
                "-leave":"leave",
                "-owner":"owner",
                "-request":"request",
                "-subscribe":"subscribe",
                "-unsubscribe":"unsubscribe"
            }

def handler(recipient):
    for mlist in LISTS:
        if recipient.startswith(mlist):
            for candidate in handlers.keys():
                if recipient[len(mlist):recipient.index("@")] == candidate:
                    return (mlist, handlers[candidate])
            return (mlist, None)
    return None

def delete(cursor, mail):
    cursor.execute("DELETE FROM mailbox WHERE mail_id = ?;", (mail, ))

def handle(cursor, mail):
    cursor.execute("SELECT mail_envelopeto, mail_data FROM mailbox WHERE mail_id = ?;", (mail, ))
    data = cursor.fetchone()

    #get handler
    info = handler(data[0])
    if info is None:
        print("Failed to handle mail for ", data[0])
        return
    
    #post mail
    if info[1] is not None:
        mm = subprocess.Popen([MAILMAN, info[1], info[0]], stdin=subprocess.PIPE)
        mm.stdin.write(bytes(data[1], 'UTF-8'))
        mm.stdin.close()
        mm.wait()

    #delete mail
    delete(cursor, row[0])

    print("Handled mail", mail, "for list ", info[0], " with handler ", info[1])

db = sqlite3.connect(DATABASE, isolation_level=None)
cursor = db.cursor()

cursor.execute("SELECT mail_id FROM mailbox WHERE mail_user = ?;", (USER, ))
rows = cursor.fetchall()
for row in rows:
    handle(cursor, row[0])
