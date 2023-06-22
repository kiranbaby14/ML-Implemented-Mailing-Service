from django.core.mail import EmailMessage
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from celery import Celery
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def send_email_with_pdf_attachment(smtp_server, smtp_port, smtp_username,
                                   smtp_password, sender_email, recipient_email,
                                   subject, body, pdf_url):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(requests.get(pdf_url).content)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename="document.pdf")
    msg.attach(attachment)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))


def send_weekly_emails():
    # Define your SMTP server and authentication details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = os.environ.get('SMTP_USERNAME')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    # Define email details
    sender_email = os.environ.get('SMTP_USERNAME')
    recipient_email = "RECEIPIENT_EMAIL"
    subject = "Weekly Email with PDF attachment"
    body = "Please find attached the weekly PDF document."
    pdf_url = "https://www.africau.edu/images/default/sample.pdf"

    # Send the email with PDF attachment
    send_email_with_pdf_attachment(smtp_server, smtp_port, smtp_username,
                                   smtp_password, sender_email, recipient_email,
                                   subject, body, pdf_url)
