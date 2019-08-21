import smtplib
from email.mime.text import MIMEText
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def send_mail(body_text=None):
    smtp_server = smtplib.SMTP_SSL(host=config['MAIL']['smtphost'], port=config['MAIL']['smtpport']) # my mail provider uses SSL, you might need to use smtplib.SMTP when your mail provider uses TLS
    smtp_server.ehlo()
    smtp_server.login(config['MAIL']['smtpuser'], config['MAIL']['smtppassword'])
    msg = MIMEText(body_text)
    msg['From'] = config['MAIL']['from_addr']
    msg['To'] = config['MAIL']['to_addr']
    msg['Subject'] = config['MAIL']['subject']
    smtp_server.send_message(msg)
    smtp_server.quit()
