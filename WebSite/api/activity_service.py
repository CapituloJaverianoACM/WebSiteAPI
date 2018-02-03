from django.http import Http404

from ..models import Activity


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
        return Activity.objects.get(id=id)
    except Activity.DoesNotExist:
        return None
