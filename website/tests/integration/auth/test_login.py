from website.tests.base_test import BaseTest, db
from website.models import User
from flask_login import current_user

class TestLogin(BaseTest):
    def test_login_post_with_valid_user(self):
        # get app
        with self.app:
            with self.app_context():
                #create a user
                response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='Tester', password1='testing', password2='testing')
                                         , follow_redirects=True)
                #assert user is created
                user = db.session.query(User).filter_by(email='test@gmail.com').first()
                self.assertTrue(user)
                self.assertTrue(current_user.is_active)
                self.app.get('/log-out', follow_redirects=True)
                self.assertFalse(current_user.is_active)
                # post to login user
                response2 = self.app.post('/log-in', data=dict(email='test@gmail.com', password='testing'), follow_redirects=True)
                self.assertTrue(current_user.is_active)
                # assert that user has logged in with a flash message
                self.assertIn(b'Logged in successfully', response2.data)

    def test_log_in_post_with_non_existent_user(self):
        with self.app:
            with self.app_context():
                response = self.app.post('/log-in', data=dict(email='test@gmail.com', password='testing'))

                user = db.session.query(User).filter_by(email='test@gmail.com').first()
                self.assertFalse(user)
                self.assertIn(b'Email does not exist', response.data)

    def test_log_in_post_with_valid_user_and_wrong_password(self):
        with self.app:
            with self.app_context():
                self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='Tester', password1='testing', password2='testing')
                                         , follow_redirects=True)
                user = db.session.query(User).filter_by(email='test@gmail.com').first()
                self.assertTrue(user)
                self.assertTrue(current_user.is_active)

                db.session.add(user)
                db.session.commit()

                self.app.get('/log-out', follow_redirects=True)
                self.assertFalse(current_user.is_active)

                response = self.app.post('/log-in', data=dict(email='test@gmail.com', password='tesing'), follow_redirects=True)
                self.assertFalse(current_user.is_active)
                self.assertIn( b'password incorrect', response.data)










