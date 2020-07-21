# -- coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render

from .services import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

# Create your views here.
from .serializers import AwardSerializer


@api_view(['POST'])
def send_question_email(request):
    message = request.POST['message']
    email = request.POST['email']
    subject = 'Contact Us Form'
    data = {
        'body_message': message,
    }
    content = render_template('contact_us.html', data)
    send_email(
        subject,
        content,
        receivers=[get_sender_email()]
    )

    content_response = render_template(
        'contact_us_response.html',
        None
    )
    send_email(subject, content_response, receivers=[email])

    response = {
        'message': 'Se ha enviado el mensaje.'
    }
    return Response(response)


def page_not_found(request, exception):
    return render(request=request, template_name='404.html', status=400)


class AwardList(APIView):

    def get(self, request):
        awards_serializer = AwardSerializer(
            get_awards(),
            many=True
        )
        return Response(
            awards_serializer.data,
            status=status.HTTP_200_OK
        )
