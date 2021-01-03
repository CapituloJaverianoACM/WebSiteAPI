from django.conf import settings
import base64
from django.core.files.storage import FileSystemStorage


def encode_media(file_name):
    """ Method that encodes a media file to base 64
    Parameters:
    file_name (string): name of the file localed in
    the media folder (NOT absolute path)

    Returns:
    string: raw file data encoded in base 64
    """
    prefix = settings.MEDIA_ROOT + '/'
    complete_path = prefix + file_name
    with open(complete_path, "rb") as image_file:
        image_str = base64.b64encode(image_file.read())
    return image_str


def upload_file(request, name):
    file_form = request.FILES[name]
    fs = FileSystemStorage()
    filename = fs.save(file_form.name, file_form)
    return filename
    #uploaded_file_url = fs.url(filename)
    #return uploaded_file_url


class BaseInlineMixin:
    extra = 0
    can_delete = False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
