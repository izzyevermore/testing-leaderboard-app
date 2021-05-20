from website.models import Note
from website.tests.base_test import BaseTest
from website import db

class NoteTest(BaseTest):
    def test_crud(self):
        with self.app.app_context():
            note = Note(data="Tester Test", date=17/5/2021, user_id=1)

            db.session.query_property(Note).filter_by(data='Tester Test').first()

