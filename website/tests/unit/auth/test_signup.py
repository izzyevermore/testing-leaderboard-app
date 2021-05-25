from flask import request
from website.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from website.models import User


# Test sign up
class TestSignUp(BaseTest):
    # Test that everyone can access the routes
    def test_get_sign_up(self):
        with self.app:
            # Goes the route
            response = self.app.get('/sign-up', follow_redirects=True)
            # assert that the route name is correct
            self.assertIn('/sign-up', request.url)
            #assert that signup page is rendered with correct content
            self.assertIn(b'<title>\nSign Up\n</title>', response.data)

            #assert that the status code is 200
            self.assertEqual(response.status_code, 200)


            # assert that no user is signed in
            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

    # test/signup post reg with an email less than 4 characters
    def test_signup_post_with_short_email(self):
        with self.app:
            # create signup post
            response = self.app.post('/sign-up', data=dict(email='me', first_name='Tester', password='testing',
                                                follow_redirects=True))
            # assert that flash message is returned
            self.assertIn(b'Email must be greater than 3 characters', response.data)
            # #assert_status_code_error
            self.assertIs(response.status_code, 200)
            # assert user is not created
            user = db.session.query(User).filter_by(email='me').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id(), AnonymousUserMixin.get_id(self))

    def test_sign_up_post_with_short_name(self):
        with self.app:
            #create a post
            response = self.app.post('/sign-up', data=dict(email='test@gmail', firstName='T', password='testing',
                                                follow_redirects=True))
            # assert the flash message appears
            self.assertIn(b'First name must be greater than 1 character', response.data)

            #assert status code
            self.assertEqual(response.status_code, 200)

            # assert user is not created
            user = db.session.query(User).filter_by(email='test@gmail').first()
            self.assertFalse(user)

            #assert user is not logged in
            self.assertIsNone(current_user.get_id())

