import os
import smtplib
from email.mime.text import MIMEText

from_addr = 'info@matthiasgass.de'
to_addr = 'gass.matthias@googlemail.com'
subject = 'Discogs Detective'

MAIL_USER = os.getenv('MAIL_USER')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


def send_mail(body_text=None):
    smtp_server = smtplib.SMTP_SSL(host='smtp.1blu.de', port=465)
    smtp_server.ehlo()
    smtp_server.login(MAIL_USER, MAIL_PASSWORD)
    msg = MIMEText(body_text)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    smtp_server.send_message(msg)
    smtp_server.quit()
