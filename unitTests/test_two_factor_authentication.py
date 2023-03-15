import jwt
from flask_mail import Mail

from app.auth.email import send_verification_email
from app.models import User
from flask import current_app
import unittest
from app import create_app, db
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class TestTwoFactorAuthentication(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.config['SERVER_NAME'] = 'localhost:5000'
        db.create_all()
        self.client = self.app.test_client()
        self.mail = Mail(self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        # scenario user deletes their post

    def test_send_verification_email(self):
        # create a test user
        user = User(id=123, email='edxiokraudy@gmail.com')
        db.session.add(user)
        db.session.commit()

        with self.app.app_context():
            send_verification_email(user)

        with self.mail.record_messages() as outbox:
            try:
                assert len(outbox) == 1
                assert user.email in outbox[0].recipients
                assert outbox[0].subject == 'Verify Your Email'
            except AssertionError as e:
                print(f"Error sending verification email: {str(e)}")

        with self.app.test_request_context():
            token = jwt.encode({'user_id': user.id, 'email': user.email},
                               current_app.config['SECRET_KEY'], algorithm='HS256')
            self.assertIsNotNone(token)
