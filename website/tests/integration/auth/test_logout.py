from flask_login import current_user

from website.tests.base_test import BaseTest, db
from website.models import User


class TestLogout(BaseTest):
    def test_log_out_route_is_accessed_when_user_is_logged_in(self):
        with self.app:
            with self.app_context():
                # create a user
                self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='Tester', password1='testing', password2='testing')
                            , follow_redirects=True)
                # assert that user has been created
                user = db.session.query(User).filter_by(email='test@gmail.com').first()
                self.assertTrue(user)
                self.assertTrue(current_user.is_active)

                # get log out route
                self.app.get('/log-out', follow_redirects=True)

                # assert that user is not active
                self.assertFalse(current_user.is_active)

    def test_resp_when_navigating_to_logout_page(self):
        with self.app:
            with self.app_context():
                self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='Tester', password1='testing', password2='testing')
                            , follow_redirects=True)

                self.assertTrue(current_user)
                self.assertTrue(current_user.is_active)
                # user becomes automatically logged in after signing-up

                response = self.app.get('/log-out', follow_redirects=True)
                self.assertEqual(response.status_code, 200)

    def test_current_user_is_none_after_logging_out(self):
        with self.app:
            with self.app_context():
                self.app.post('/sign-up')

