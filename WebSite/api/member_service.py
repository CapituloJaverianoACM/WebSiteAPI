from ..models import Member


def getStaff():
	membersStaff = Member.objects.filter(is_staff=True).order_by('position')
	return membersStaff


def check_unique_email(email):
	"""
	:param email: str
	:return: boolean
	"""
	return Member.objects.filter(email=email).count() == 0


def get_candidates():
	"""
	:return: QuerySet<Member>
	"""
	return Member.objects.filter(date_chapter=None)
