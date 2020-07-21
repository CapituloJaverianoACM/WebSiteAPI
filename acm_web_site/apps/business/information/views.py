# -- coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import date
from .models import *

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

# Create your views here.

@api_view(['POST'])
def send_question_email(request):
	message = request.POST['message']
	email = request.POST['email']
	subject = 'Contact Us Form'
	data = {
		'body_message': message,
	}
	content = email_service.render_template('contact_us.html', data)
	email_service.send_email(
		subject,
		content,
		receivers=[email_service.get_sender_email()]
	)

	content_response = email_service.render_template(
		'contact_us_response.html',
		None
	)
	email_service.send_email(subject, content_response, receivers=[email])

	response = {
		'message': 'Se ha enviado el mensaje.'
	}
	return Response(response)


def page_not_found(request, exception):
	return render(request=request, template_name='404.html', status=400)


class AwardList(APIView):

	def get(self, request):
		awards_serializer = AwardSerializer(
			award_service.get_awards(),
			many=True
		)
		return Response(
			awards_serializer.data,
			status=status.HTTP_200_OK
		)

class MemberViewSet(viewsets.ViewSet):

	def get_queryset(self, filter=None, exclude=None, order_by=None):
		members = Member.objects.all()
		is_staff = self.request.query_params.get('isStaff', None)

		filter = filter or dict()

		if is_staff is not None:
			filter.update(dict(is_staff=is_staff))

		if exclude is not None and isinstance(exclude, dict):
			members = members.exclude(**exclude)
		if filter is not None and isinstance(filter, dict):
			members = members.filter(**filter)
		if order_by is not None and isinstance(order_by, list):
			members = members.order_by(*order_by)
		return members

	def list(self, request):
		member_serializers = MemberSerializer(
			self.get_queryset(),
			many=True
		)
		return Response(
			member_serializers.data,
			status=status.HTTP_200_OK
		)

	def create(self, request):
		member_serializer = MemberSerializer(data=self.request.data)
		if member_serializer.is_valid():
			member_serializer.create(member_serializer.data)
			return Response(
				member_serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			member_serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)

join_us = MemberViewSet.as_view(dict(post='create'))