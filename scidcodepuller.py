import email
import imaplib
import os
import pyperclip
from dotenv import load_dotenv as dotenv
from time import time, sleep

def code():
    recent = "recent.txt"
    with open(recent) as f:
        recentcode = f.read()
    code1 = recentcode
    code2 = recentcode
    s = time()
    e = time()
    while (code1 == recentcode or code2 == recentcode) and e-s <= 6:
        host = 'imap.gmail.com'
        username = os.getenv("email")
        password = os.getenv("passw")
        mail = imaplib.IMAP4_SSL(host)
        mail.login(username, password)
        mail.select('inbox')
        _, search_data = mail.search(None, 'ALL')
        num1 = search_data[0].split()[-1]
        num2 = search_data[0].split()[-2]
        _, data1 = mail.fetch(num1, '(BODY.PEEK[HEADER])')
        _, data2 = mail.fetch(num2, '(BODY.PEEK[HEADER])')
        _, b1 = data1[0]
        _, b2 = data2[0]
        e_m1 = email.message_from_bytes(b1)
        e_m2 = email.message_from_bytes(b2)
        it1 = e_m1.items()
        it2 = e_m2.items()
        subject1 = it1[16][1]
        subject2 = it2[16][1]
        code1 = subject1[-8:-1]
        code2 = subject2[-8:-1]
        code1 = code1.replace(' ', '')
        code2 = code2.replace(' ', '')
        try:
            int(code1)
            with open(recent, 'w') as f:
                f.write(code1)
            pyperclip.copy(code1)
        except:
            int(code2)
            with open(recent, 'w') as f:
                f.write(code2)
            pyperclip.copy(code2)
        e=time()
        #print(e-s)
if __name__ == '__main__':
    code()
