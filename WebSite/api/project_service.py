from ..models import Project


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
