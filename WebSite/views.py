from django.shortcuts import render, redirect
from datetime import datetime, date
from django.http import JsonResponse
from .models import *
from WebSite.api import award_service
from WebSite.api import member_service
from WebSite.api import email_service


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
		'state': 'Se ha enviado el mensaje.'
	}
	# TODO Clear the form
	return JsonResponse(response)


def send_join_form(request):
	# TODO See if add another table for this people
	# TODO Clear the form
	name = request.POST['names']
	last_name = request.POST['surnames']
	email = request.POST['email']
	major = request.POST['major']
	reason = request.POST['reason']
	data = {
		'state': '¡Nos alegra que quieras hacer parte del capitulo!'
	}
	return JsonResponse(data)


def page_not_found(request):
	return render(request=request, template_name='404.html', status=400)
