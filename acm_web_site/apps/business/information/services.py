from os import environ
import threading

from django.template import loader, TemplateDoesNotExist, TemplateSyntaxError
from django.core.mail import EmailMessage
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from .models import Award, Member


def get_awards():
    return Award.objects.all()


class EmailThread(threading.Thread):
    def __init__(self, subject, content, receivers=None, sender=None):
        self.subject = subject
        self.receivers = receivers or [get_receiver_email()]
        self.content = content
        self.sender = sender or get_sender_email()
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(
            subject=self.subject,
            body=self.content,
            from_email=self.sender,
            to=self.receivers
        )
        message.content_subtype = 'html'
        message.send()


def send_email(subject, content, sender=None, receivers=None):
    """
    :param subject: str
    :param content: str
    :param sender: str
    :param receivers: list
    :return:
    """
    EmailThread(subject, content, receivers, sender).start()


def get_sender_email():
    return environ.get('DEFAULT_SENDER_EMAIL', '')


def get_receiver_email():
    return environ.get('DEFAULT_RECEIVER_EMAIL', '')


def render_template(template_path, data):
    rendered = ""
    try:
        template = loader.get_template(template_path)
        rendered = template.render(data)
    except TemplateDoesNotExist:
        print('The template {0} could not be found'.format(template_path))
    except TemplateSyntaxError:
        print('The template {0} could not be found'.format(template_path))
    return rendered


def get_staff():
    # TODO - send the path
    membersStaff = Member.objects.filter(is_staff=True).order_by('position'). \
        values(
        'name',
        'surname',
        'email',
        'major',
        'id_photo_id',
        'is_staff',
        'position',
        'description',
    )
    return membersStaff


def check_unique_email(email):
    """
    :param email: str
    :return: boolean
    """
    return Member.objects.filter(email=email).count() == 0


def get_candidates():
    """
    :return: QuerySet<Member>
    """
    return Member.objects.filter(date_chapter=None)


def get_member_by_id(id):
    try:
        member = Member.objects.get(id=id)
    except MultipleObjectsReturned:
        member = None
    except ObjectDoesNotExist:
        member = None
    return member


def get_member_by_email(email):
    """
    :param email: str
    :return: Member
    """
    try:
        member = Member.objects.get(email=email)
    except MultipleObjectsReturned:
        member = None
    except ObjectDoesNotExist:
        member = None
    return member
