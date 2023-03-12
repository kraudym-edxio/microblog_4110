import jwt
from flask import render_template, url_for, current_app
from flask_babel import _

from app.email import send_email
from flask_mail import Message
from app import mail


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Microblog] Reset Your Password'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))


def send_verification_email(user):
    # generate a token for the user
    payload = {'user_id': user.id, 'email': user.email}
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")

    # set up the message
    subject = 'Verify Your Email'
    sender = current_app.config['ADMINS'][0]
    recipient = user.email
    html_body = render_template('email/verification_email.html', token=token)

    # send the message
    msg = Message(subject, sender=sender, recipients=[recipient])
    msg.html = html_body
    mail.send(msg)
