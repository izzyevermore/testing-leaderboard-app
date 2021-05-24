from website.tests.base_test import BaseTest, db
from website.models import Team

class TeamTest(BaseTest):
    def test_crud_team(self):
        with self.app_context():
            team = Team(id=1, name='QATeam')

            results = db.session.query(Team).filter_by(name='QATeam').first()
            self.assertIsNone(results)

            db.session.add(team)
            db.session.commit()

            results = db.session.query(Team).filter_by(name='QATeam').first()
            self.assertIsNotNone(results)

            db.session.delete(team)
            db.session.commit()

            results = db.session.query(Team).filter_by(name='QATeam').first()
            self.assertIsNone(results)