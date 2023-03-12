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

class TestFavouriteArchive(unittest.TestCase):
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



    # scenario user archives a post
    def test_add_favourite(self):
        # create test user
        u = User(username='testuser', email='testuser@example.com')
        db.session.add(u)
        db.session.commit()

        # create test favourite
        f = Favourite(body='test body', user_id=u.id)
        db.session.add(f)
        db.session.commit()

        # retrieve favourite from database
        fav = Favourite.query.filter_by(user_id=u.id).first()

        # check that favourite was saved correctly
        self.assertEqual(fav.body, 'test body')
        self.assertEqual(fav.user_id, u.id)

    # scenario user deletes their post
    def test_delete_post_favourite(self):
        # create test user
        u1 = User(username='testuser1', email='testuser1@example.com')
        db.session.add(u1)
        db.session.commit()

        u2 = User(username='testuser2', email='testuser2@example.com')
        db.session.add(u2)
        db.session.commit()

        # create test post
        p = Post(body='test body', user_id=u1.id)
        db.session.add(p)
        db.session.commit()

        f = Favourite(body=p.body, user_id=p.user_id,current_id=u2.id)
        db.session.add(f)
        db.session.commit()

        post = Post.query.get(p.id)
        db.session.delete(post)
        db.session.commit()
        

        self.assertEqual(f.body, 'test body')

    # scenario user views their favourites
    def test_user_views_favourites(self):
        # Create a test user
        user = User(username='test_user', email='test@example.com')
        user.set_password('test')
        db.session.add(user)
        db.session.commit()

        # Login the user
        response = self.client.post(
            '/auth/login',data={'id': 'test_user', 'name': 'test'})
        self.assertEqual(response.status_code, 200)

        # Access the favorites endpoint
        response = self.client.get('/favourites', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Favourites', response.data)