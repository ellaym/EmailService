from flask_mail import Message
from flask import current_app
from app import mail

def send_email(to_email, subject, message):
    """
    Function to send an email using Flask-Mail.

    Args:
        to_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        message (str): The content of the email.

    Returns:
        None
    """
    # Use current_app to access the application context
    msg = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to_email])
    msg.body = message
    mail.send(msg)
