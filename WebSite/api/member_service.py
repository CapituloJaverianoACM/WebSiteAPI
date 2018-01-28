from ..models import Member


def getStaff():
	membersStaff = Member.objects.filter(is_staff=True).order_by('position')
	return membersStaff


def check_unique_email(email):
	return Member.objects.filter(email=email).count() == 0
