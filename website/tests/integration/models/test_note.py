from website.models import Note
from website.tests.base_test import BaseTest

class NoteTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            note = Note(id=1, data="Tester Test")

            note.home()

            self.assertIsNotNone(Note.find_by_name('Tester Test'))

