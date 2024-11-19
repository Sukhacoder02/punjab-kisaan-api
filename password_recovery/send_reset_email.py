# password_recovery/send_reset_email.py

import re
from datetime import datetime, timedelta
import jwt
import smtplib
from email.mime.text import MIMEText

# Constants and configurations
SECRET_KEY = 'your_secret_key'
JWT_EXPIRATION_MINUTES = 30
EMAIL_SENDER = 'no-reply@yourapp.com'
SMTP_SERVER = 'smtp.yourapp.com'
SMTP_PORT = 587
SMTP_USERNAME = 'smtp_username'
SMTP_PASSWORD = 'smtp_password'
RESET_LINK_TEMPLATE = 'https://yourapp.com/reset-password?token={token}'

# Helper functions
def validate_email_address(email):
    """ Validate the email address format. """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def generate_reset_token(email):
    """ Generate a JWT token for password reset. """
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def send_email(to_address, subject, body):
    """ Send an email using SMTP. """
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = to_address

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, to_address, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function
def request_password_reset(email):
    """ Handle the user's request for a password reset. """
    if not validate_email_address(email):
        return {'status': 'error', 'message': 'Invalid email address.'}

    token = generate_reset_token(email)

    reset_link = RESET_LINK_TEMPLATE.format(token=token)
    email_body = f"""
    <p>Hello,</p>
    <p>You requested to reset your password. Please click the link below to reset your password:</p>
    <p><a href="{reset_link}">Reset Password</a></p>
    <p>If you did not request a password reset, please ignore this email.</p>
    """

    try:
        send_email(email, "Password Reset Request", email_body)
        return {'status': 'success', 'message': 'Password reset email sent.'}
    except Exception as e:
        return {'status': 'error', 'message': f'Failed to send email: {e}'}
