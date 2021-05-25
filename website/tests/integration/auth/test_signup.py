from website.tests.base_test import BaseTest, db
from website.models import User


class TestSignup(BaseTest):
    # creating a post user successfully
    def test_sign_up_post_success(self):
        with self.app:
            # creating a post with valid data
            response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='Tester', password1='testing', password2='testing')
                                     , follow_redirects=True)
            #assert that new user is created
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertTrue(response)

            #save to db
            db.session.add(user)
            db.session.commit()

            #assert to see if it exists in the database
            self.assertTrue(user)

            #assert if flash message appears
            self.assertIn(b'Account created', response.data)