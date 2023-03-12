from app.models import User, Post, Favourite
from flask import render_template, current_app
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from config import Config
from app.auth.routes import login

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None

class TestDeletePost(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # scenario user deletes post 
    def test_delete_post(self):
        # create test user
        u = User(username='testuser', email='testuser@example.com')
        db.session.add(u)
        db.session.commit()

        # create test post
        p = Post(body='test body', user_id=u.id)
        db.session.add(p)
        db.session.commit()

        # delete test post
        db.session.delete(p)
        db.session.commit()

        deleted_post = Post.query.filter_by(id=p.id).first()
        assert deleted_post is None



