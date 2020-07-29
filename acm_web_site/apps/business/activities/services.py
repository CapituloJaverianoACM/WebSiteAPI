from .models import (
    Activity,
    Project,
    Tutorial,
    ActivityMember
)
from business.people.services import get_member_by_id


def get_all_activities():
    """
    :return: QuerySet<Actitvity>
    """
    return Activity.objects.order_by('date')


def get_activity(activity_id):
    """
    :param activity_id: int
    :return: Activity obj
    """
    try:
        return Activity.objects.get(id=activity_id)
    except Activity.DoesNotExist:
        return None


def create_activity_member(
        id_activity,
        id_member,
        role) -> Activity:

    activity = get_activity(id_activity)
    member = get_member_by_id(id_member)
    activity_member = ActivityMember(
        member=member,
        activity=activity,
        role=role,
    )
    activity_member.full_clean()
    activity_member.save()

    return get_activity(id_activity)


def get_projects():
    return Project.objects.all()


def get_project(id):
    """
    :param id: int
    :return: Project
    """
    try:
        return Project.objects.get(id=id)
    except Project.DoesNotExist:
        return None


def get_tutorials():
    return Tutorial.objects.all()


def get_tutorial(id):
    """
    :param id: int
    :return: Project
    """
    try:
        return Tutorial.objects.get(id=id)
    except Tutorial.DoesNotExist:
        return None
