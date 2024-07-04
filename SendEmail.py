import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_ADDRESS = 'abc@gmail.com' #add your gmail account
EMAIL_PASSWORD = '' #add you gmail account password (if fails use app password from google, instructions present in readme.md)
ATTACHMENT_PATH = './abc.pdf' #add path to the attachment

def send_email(to_email):
    msg = EmailMessage()
    msg['Subject'] = 'Subject' #add subject here
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    body = """\
    Add message body here
    """

    msg.set_content(body)

    with open(ATTACHMENT_PATH, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(ATTACHMENT_PATH)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print(f'Email sent to {to_email}')

def main():
    #add email receivers email addresses
    email_list = [
        'xyz@gmail.com',
        'loremipsum@gmail.com'
    ]

    for email in email_list:
        send_email(email)

if __name__ == '__main__':
    main()
