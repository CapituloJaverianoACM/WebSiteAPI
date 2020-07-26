import pdb

from django.test import TestCase

from mixer.backend.django import mixer

from business.people.models import Team, Member
from business.people.services import get_member_by_email


class GetMemberByEmail(TestCase):

    def setUp(self):
        self.member = mixer.blend(Member, email="camilo@serrano.com")
        self.member = mixer.blend(Member, email="juan@prez.com")

    def test_should_get_member(self):
        response = get_member_by_email("juan@perez.com")
        self.assertEquals(response, self.member)

    def test_should_get_no_member(self):
        response = get_member_by_email("akjbsf@fasd.esf")
        self.assertEquals(response, None)
