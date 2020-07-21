from .models import Team, Member
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def get_teams():
    """
    :return: QuerySet<Team>
    """
    return Team.objects.all()


def get_staff():
    # TODO - send the path
    membersStaff = Member.objects.filter(is_staff=True).order_by('position'). \
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


def get_member_by_id(id):
    try:
        member = Member.objects.get(id=id)
    except MultipleObjectsReturned:
        member = None
    except ObjectDoesNotExist:
        member = None
    return member


def get_member_by_email(email):
    """
    :param email: str
    :return: Member
    """
    try:
        member = Member.objects.get(email=email)
    except MultipleObjectsReturned:
        member = None
    except ObjectDoesNotExist:
        member = None
    return member
