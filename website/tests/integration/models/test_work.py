from website.tests.base_test import BaseTest, db
from website.models import Work

class WorkTest(BaseTest):
    def test_crud_work(self):
        with self.app_context():
            work = Work(title='Tester Test', description='Testing', user_id=1, status='Testing', points=20)

            results = db.session.query(Work).filter_by(description='Testing').first()
            self.assertIsNone(results)

            db.session.add(work)
            db.session.commit()

            results = db.session.query(Work).filter_by(description='Testing').first()
            self.assertIsNotNone(results)

            db.session.delete(work)
            db.session.commit()

            results = db.session.query(Work).filter_by(description='Testing').first()
            self.assertIsNone(results)


