from website.models import Note
from website.tests.base_test import BaseTest, db
from unittest import TestCase

# This is a class that tests if models can be saved and deleted from the database
class NoteTest(BaseTest):
    def test_crud_note(self):
        # This bottom line of code calls the app_context
        with self.app_context():
            # Test that notes can be added and delted from the database
            note = Note(id=1, data="Testing")

            #assert that this note does not exists in the database
            results = db.session.query(Note).filter_by(data="Testing").first()
            self.assertIsNone(results)

            #save to db
            db.session.add(note)
            db.session.commit()


            #assert that is does exist in the database
            results = db.session.query(Note).filter_by(data="Testing").first()
            self.assertIsNotNone(results)


            #delete from db
            db.session.delete(note)
            db.session.commit()

            #assert that note is no longer in db
            results = db.session.query(Note).filter_by(data="Testing").first()
            self.assertIsNone(results)
