from ..models import Tutorial


def get_tutorials():
    return Tutorial.objects.all()
