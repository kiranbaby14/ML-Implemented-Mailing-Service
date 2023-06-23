from django.core.mail import EmailMessage
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from celery import shared_task
import requests
from dotenv import load_dotenv
import os
import time
from backend.celery import app
import datetime
from django.conf import settings

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


@app.task(name="send_weekly_emails")
def send_weekly_emails():
    try:
        # Define your SMTP server and authentication details
        smtp_server = settings.EMAIL_HOST
        smtp_port = settings.EMAIL_PORT
        smtp_username = settings.EMAIL_HOST_USER
        smtp_password = settings.EMAIL_HOST_PASSWORD

        # Define email details
        sender_email = os.environ.get('SMTP_USERNAME')
        recipient_email = os.environ.get('RECEIPIENT_EMAIL')
        subject = "Weekly Email with PDF attachment"
        body = "Please find attached the weekly PDF document."
        pdf_url = "https://www.africau.edu/images/default/sample.pdf"

        # Send the email with PDF attachment
        send_email_with_pdf_attachment(smtp_server, smtp_port, smtp_username,
                                       smtp_password, sender_email, recipient_email,
                                       subject, body, pdf_url)
    except:
        print("error")


# @app.task(name="send_weekly_email")
# def send_weekly_email():
#     try:
#         today = datetime.date.today()
#         week_ago = today - datetime.timedelta(days=7)
#     except:
#         print("error")


@shared_task
def sleepy(duration):
    time.sleep(duration)
    return None
