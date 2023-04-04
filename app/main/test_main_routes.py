from flask import render_template, current_app
import unittest
from app import create_app, db
from config import Config
from app.auth.routes import loginLocust, registerLocust


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class TestMainRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_sitemap(self):
        with self.app.test_client() as c:
            headers = {"Content-Type": "application/json"}
            response = c.get('/branches', headers=headers)
            self.assertEqual(response.status_code, 200)
