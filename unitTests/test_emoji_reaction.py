from app.models import User, Post, Reaction
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

class TestPostReactions(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        # scenario user deletes their post
    def test_react_to_post(self):
        # create test user
        u1 = User(username='testuser1', email='testuser1@example.com')
        db.session.add(u1)
        db.session.commit()

        # create test post
        post = Post(body='test post', user_id=u1.id)
        db.session.add(post)
        db.session.commit()

        # create test reaction
        react = Reaction(post_id=post.id, user_id=u1.id, reaction_type="like")
        db.session.add(react)
        db.session.commit()

        # get the updated post from the db
        new_post=Post.query.get(post.id)
        new_post.reaction_like+=1;
        db.session.add(new_post)
        db.session.commit()

        self.assertEqual(new_post.reaction_like, 1)