# -- coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import date
from .models import *

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .api import (
	activity_service,
	award_service,
	tutorial_service,
	project_service,
	email_service
)

from acm_web_site.apps.business.people.serializer.member_serializer import MemberSerializer
from .serializer.activity_serializer import ActivitySerializer
from .serializer.activity_serializer import ConfirmActivitySerializer
from .serializer.tutorial_serializer import TutorialSerializer
from .serializer.project_serializer import ProjectSerializer
from .serializer.award_serializer import AwardSerializer


def index(request):
	awards = award_service.get_awards().order_by('-date')
	recent_activities = []
	order_to_future = Activity.objects.exclude(
		date__lt=date.today()
	).order_by('date')
	for activity in order_to_future:
		recent_activities.append(activity)
		if len(recent_activities) == 3:
			break
	order_to_past = Activity.objects.exclude(
		date__gt=date.today()
	).order_by('-date')
	for activity in order_to_past:
		recent_activities.append(activity)
		if len(recent_activities) == 6:
			break
	our_projects = []
	projects = Project.objects.order_by('-dateEnd')
	for project in projects:
		if len(our_projects) == 5:
			break
		our_projects.append(project)
	context = {
		'awards': awards,
		'recentActivities': recent_activities,
		'our_projects': our_projects
	}
	return render(request, 'index.html', context)


@api_view(['POST'])
def test(request):
	response = {
		'msg': 'Estamos conectados'
	}
	return Response(response)


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


class ActivityList(APIView):

	def get(self, request):
		activities_serializer = ActivitySerializer(
			activity_service.get_all_activities(),
			many=True
		)
		return Response(
			activities_serializer.data,
			status=status.HTTP_200_OK
		)


class ActivityDetail(APIView):

	def get(self, request, id):
		activity = activity_service.get_activity(id)
		activity_serializer = ActivitySerializer(activity)
		if activity_serializer:
			return Response(activity_serializer.data)
		else:
			errors = dict(message='La actividad no se ha encontrado')
			return Response(
				errors,
				status=status.HTTP_404_NOT_FOUND
			)

	def post(self, request, pk):
		member_serializer = MemberSerializer(data=request.data)
		print(member_serializer)
		# TODO: Handle all info received from form
		# TODO: Save the many to many relationship in serializer


class ConfirmActivityView(GenericAPIView):
	serializer_class = ConfirmActivitySerializer

	def post(self, request, uidb64=None, token=None):
		serializer_data = self.request.data
		serializer_data.update({
			'uidb64': uidb64,
			'token': token
		})
		serializer = self.get_serializer(data=self.request.data)
		serializer.is_valid(raise_exception=True)

		# TODO: Add logic to confirm the assistance
		"""
		uid = urlsafe_base64_decode(uidb64)
		user = User.objects.get(pk=uid)
		password = serializer.data.get('password1')
		user.set_password(password)
		user.save()
		"""
		return Response('OK')


class TutorialList(APIView):

	def get(self, request):
		tutorial_serializer = TutorialSerializer(
			tutorial_service.get_tutorials(),
			many=True
		)
		return Response(
			tutorial_serializer.data,
			status=status.HTTP_200_OK
		)


class TutorialDetail(APIView):

	def get(self, request, id):
		tutorial = tutorial_service.get_tutorial(id=id)
		tutorial_serializer = ProjectSerializer(tutorial)
		return Response(
			tutorial_serializer.data,
			status=status.HTTP_200_OK
		)


class ProjectList(APIView):

	def get(self, request):
		project_serializer = ProjectSerializer(
			project_service.get_projects(),
			many=True
		)
		return Response(
			project_serializer.data,
			status=status.HTTP_200_OK
		)


class ProjectDetail(APIView):

	def get(self, request, id):
		project = project_service.get_project(id=id)
		project_serializer = ProjectSerializer(project)
		return Response(
			project_serializer.data,
			status=status.HTTP_200_OK
		)


