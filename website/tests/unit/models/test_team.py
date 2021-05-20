from unittest import TestCase
from website.models import Team


class TeamTest(TestCase):
    def test_create_team(self):
        team = Team(id=1, name='QATeam')

        self.assertIs(team.id, 1)
        self.assertEqual(team.name, 'QATeam')