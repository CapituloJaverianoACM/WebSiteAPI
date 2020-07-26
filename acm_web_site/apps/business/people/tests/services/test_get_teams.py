import pdb

from django.test import TestCase

from mixer.backend.django import mixer

from business.people.models import Team
from business.people.services import get_teams


class GetTeamsTest(TestCase):

    def setUp(self):
        self.teams = mixer.cycle(4).blend(Team)

    def test_shouldGetAllTeams(self):
        response = get_teams().all()
        self.assertEquals(response.count(), len(self.teams))
        for team in response:
            self.assertIn(team, self.teams)
