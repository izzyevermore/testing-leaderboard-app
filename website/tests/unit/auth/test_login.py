from website.tests.base_test import BaseTest, db
from flask import request

class TestLogin(BaseTest):
    def test_login_page_displays(self):
        with self.app:
            response = self.app.get('/log-in', follow_redirects=True)
            self.assertIn('/log-in', request.url)

    def test_login_page_returns_correct_data(self):
        with self.app:
            response = self.app.get('/log-in', follow_redirects=True)
            with self.app_context():
                self.assertIn(b'<h3 align="center">Log in</h3>', response.data)
