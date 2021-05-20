from unittest import TestCase
from website.models import User

class UserTest(TestCase):
    def test_create_user(self):
        user = User(email='test@gmail.com', password='tester', first_name='test', team_id=1, team_leader=True, points=100)

        self.assertEqual(user.email, 'test@gmail.com', "User email has been found")
        self.assertEqual(user.password, 'tester', 'Password has been made')
        self.assertEqual(user.first_name, 'test', "firstname has been made")
        self.assertIsNotNone(user.notes)
        self.assertEqual(user.team_id, 1)
        self.assertTrue(user.team_leader)
        self.assertEqual(user.points, 100)


