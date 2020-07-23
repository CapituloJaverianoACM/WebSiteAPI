from django.conf import settings
import base64


def get_picture(self, obj):
    prefix = '/'.join(settings.MEDIA_ROOT.split('/')[:-1])
    complete_path = prefix + obj.picture
    with open(complete_path, "rb") as image_file:
        image_str = base64.b64encode(image_file.read())
    return image_str
