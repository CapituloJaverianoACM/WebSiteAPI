from django.http import HttpResponse

from .models import (
    Activity,
    Project,
    Tutorial,
    ActivityMember
)
from django.core.exceptions import ObjectDoesNotExist


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


def create_or_update_activity_member(
        *,
        activity,
        member,
        role,
        is_confirmed) -> Activity:
    try:
        """Updates existing relationship"""
        activity_member = ActivityMember\
            .objects.get(activity=activity, member=member)
        activity_member.role = role
        activity_member.is_confirmed = is_confirmed
    except ObjectDoesNotExist:

        if activity.members.count() < activity.capacity:
            """Creates relationship"""
            activity_member = ActivityMember(
                member=member,
                activity=activity,
                role=role,
                is_confirmed=is_confirmed
            )
        else:
            # TODO: Handle exception
            raise Exception("Excede capacidad de la actividad")

    activity_member.full_clean()
    activity_member.save()
    return activity


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
