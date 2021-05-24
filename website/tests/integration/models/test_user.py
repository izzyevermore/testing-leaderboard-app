from website.tests.base_test import BaseTest, db
from website.models import User

class UserTest(BaseTest):
    def test_crud_user(self):
        with self.app_context():
            user = User(email='test@gmail.com', password='tester', first_name='test', team_id=1, team_leader=True, points=100)

            results = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertIsNone(results, "Has not been added to the database")

            db.session.add(user)
            db.session.commit()

            results = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertIsNotNone(results)

            db.session.delete(user)
            db.session.commit()

            results = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertIsNone(results)