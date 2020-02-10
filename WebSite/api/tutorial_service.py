from ..models import Tutorial


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
