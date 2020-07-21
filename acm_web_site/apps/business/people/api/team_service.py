from acm_web_site.apps.business.web_site.models import Team


def get_teams():
    """
    :return: QuerySet<Team>
    """
    return Team.objects.all()
