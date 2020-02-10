from WebSite.models import Team


def get_teams():
    """
    :return: QuerySet<Team>
    """
    return Team.objects.all()
