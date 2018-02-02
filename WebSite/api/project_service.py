from ..models import Project


def get_projects():
    return Project.objects.all()
