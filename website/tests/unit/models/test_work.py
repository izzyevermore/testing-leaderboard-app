from unittest import TestCase
from website.models import Work


class WorkTest(TestCase):
    def test_create_work(self):
        work = Work(title='Tester Test', description='Testing', user_id=1, status='Testing', points=20)

        self.assertEqual(work.title, 'Tester Test')
        self.assertEqual(work.description, 'Testing')
        self.assertIs(work.user_id, 1)
        self.assertEqual(work.status, 'Testing')
        self.assertIs(work.points, 20)