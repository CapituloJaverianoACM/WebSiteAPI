import pdb

from django.test import TestCase

from mixer.backend.django import mixer

from business.people.models import Team, Member
from business.people.services import get_teams, get_member_by_id


class GetTeamsTest(TestCase):

    def setUp(self):
        self.member = mixer.blend(Member, id=69)

    def test_should_get_member(self):
        response = get_member_by_id(69)
        self.assertEquals(response, self.member)

    def test_should_get_no_member(self):
        response = get_member_by_id(9)
        self.assertEquals(response, None)
