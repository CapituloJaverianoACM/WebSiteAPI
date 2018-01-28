from ..models import Activity


def get_all_activities():
    """
    :return: QuerySet<Actitvity>
    """
    return Activity.objects.order_by('date')
