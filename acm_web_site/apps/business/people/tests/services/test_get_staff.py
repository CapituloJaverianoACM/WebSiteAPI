import pdb

from django.test import TestCase

from mixer.backend.django import mixer

from business.people.models import Team, Member
from business.people.services import get_teams, get_staff


class GetTeamsTest(TestCase):
    '''def test_all_members_are_staff(self):
        self.staff = mixer.cycle(3).blend(Member, is_staff=True)
        response = get_staff().all()
        self.assertEquals(response.count(), len(self.staff))
        for team in response:
            self.assertIn(team, self.staff)'''

    '''def test_no_members_are_staff(self):
        self.staff = mixer.cycle(3).blend(Member, is_staff=False)
        response = get_staff().all()
        self.assertEquals(response.count(), 0))'''
