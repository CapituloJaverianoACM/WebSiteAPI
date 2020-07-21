from .models import (
    Activity,
    Project,
    Tutorial
)


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
