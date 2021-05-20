from unittest import TestCase
from website.models import Note

class NoteTest(TestCase):
    def test_create_note(self):
        note = Note(id=1, data='Tester Test')

        self.assertEqual(note.id, 1)
        self.assertEqual(note.data, 'Tester Test', 'success')






