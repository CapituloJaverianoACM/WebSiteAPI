import pdb

from django.test import TestCase
from django.utils import timezone

from mixer.backend.django import mixer

from business.people.models import Team, Member
from business.people.services import get_teams, get_candidates


class GetTeamsTest(TestCase):

    def setUp(self):
        self.teams = mixer.cycle(4).blend(Member, date_chapter=None)
        self.teams.append(mixer.blend(Member, date_chapter=timezone.now()))
        self.teams.append(mixer.blend(Member, date_chapter=None))

    def test_should_get_four_candidates(self):
        response = get_candidates().all()
        self.assertEquals(response.count(), 5)
