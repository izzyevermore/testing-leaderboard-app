from flask_login import current_user

from website.tests.base_test import BaseTest, db
from website.models import User

class TestLogout(BaseTest):
    def test_route_cant_be_accessed_if_user_is_not_logged_in(self):
        with self.app:
            with self.app_context():
                self.app.get('/log-out', follow_redirects=True)
                #assert that error message should display that user is not logged in
                self.assertFalse(current_user.is_active)

    def test_resp_when_user_navigates_to_logout_when_they_are_not_logged_in(self):
        with self.app:
            with self.app_context():
                response = self.app.get('/log-out', follow_redirects=True)
                self.assertEqual(response.status_code, 400)
                self.assertFalse(current_user.is_active)