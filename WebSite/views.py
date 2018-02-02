# -- coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from datetime import date
from django.http import JsonResponse
from .models import *

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

from WebSite.api import award_service
from WebSite.api import member_service
from WebSite.api import email_service
from WebSite.api import activity_service
from WebSite.api import tutorial_service
from WebSite.api import project_service

from WebSite.serializer.member_serializer import MemberSerializer
from WebSite.serializer.activity_serializer import ActivitySerializer
from WebSite.serializer.activity_serializer import ConfirmActivitySerializer
from WebSite.serializer.tutorial_serializer import TutorialSerializer
from WebSite.serializer.project_serializer import ProjectSerializer


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


def staff(request):
	staffMembers = member_service.getStaff()
	context = {
		'members': staffMembers,
	}
	return render(request, 'staff.html', context)


def contest(request):
	return render(request, 'contests.html')


def activities(request):
	return render(request, 'activities.html')


def activity_detail(request, id_activity):
	return render(request, 'activity.html')


def projects(request):
	return render(request, 'projects.html')


def project_detail(request, id_project):
	return render(request, 'project.html')


def tutorials(request):
	return render(request, 'tutorials.html')


def tutorial_detail(request, id_tutorial):
	return render(request, 'tutorial.html')


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


@api_view(['POST'])
def send_join_form(request):
	"""
	name = request.POST['names']
	last_name = request.POST['surnames']
	email = request.POST['email']
	major = request.POST['major']
	reason = request.POST['reason']
	"""
	data = {
		'state': '¡Nos alegra que quieras hacer parte del capitulo!'
	}
	return JsonResponse(data)


def page_not_found(request):
	return render(request=request, template_name='404.html', status=400)


class MemberList(APIView):

	def get(self, request):
		member_serializers = MemberSerializer(
			member_service.get_staff(),
			many=True
		)
		return Response(
			member_serializers.data,
			status=status.HTTP_200_OK
		)

	def post(self, request):
		member_serializer = MemberSerializer(data=request.data)
		if member_serializer.is_valid():
			if member_service.check_unique_email(
					request.data.get('email', '')):
				member_serializer.save()
				return Response(
					member_serializer.data,
					status=status.HTTP_201_CREATED
				)
		errors = dict(error='Ya se encuentra en uso.')
		return Response(
			errors,
			status=status.HTTP_400_BAD_REQUEST
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
		serializer = ActivitySerializer(activity)
		serializer.is_valid(raise_exception=True)
		return Response(serializer.data)

	def post(self, request, pk):
		member_serializer = MemberSerializer(data=request.data)
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
