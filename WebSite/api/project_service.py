from ..models import Project


def get_proyects():
    return Project.objects.all()
