from flask import render_template, current_app
import unittest
from app import create_app, db
from config import Config
from app.auth.routes import loginLocust, registerLocust


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class TestAuthRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_loginLocust(self):
        with self.app.test_client() as c:
            payload = {
                "username": "user",
                "password": "passw"
            }
            headers = {"Content-Type": "application/json"}
            response = c.post('/auth/loginLocust', json=payload, headers=headers)
            self.assertEqual(response.status_code, 200)

    def test_registerLocust(self):
        with self.app.test_client() as c:
            payload = {
                "username": "user",
                "email": "@test.com",
                "password": "passw",
                "is_verified": True
            }
            headers = {"Content-Type": "application/json"}
            response = c.post('/auth/registerLocust', json=payload, headers=headers)
            self.assertEqual(response.status_code, 200)