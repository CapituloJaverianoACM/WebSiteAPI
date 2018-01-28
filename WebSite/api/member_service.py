from ..models import Member


def get_staff():
	# TODO - send the path
	membersStaff = Member.objects.filter(is_staff=True).order_by('position').\
		values(
		'name',
		'surname',
		'email',
		'major',
		'id_photo_id',
		'is_staff',
		'position',
		'description',
	)
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
