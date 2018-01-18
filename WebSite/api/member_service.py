from ..models import Member


def getStaff():
	membersStaff = Member.objects.filter(is_staff=True).order_by('position')
	return membersStaff
