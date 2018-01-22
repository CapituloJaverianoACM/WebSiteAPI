from django.shortcuts import render, redirect
from datetime import datetime, date
from django.core.mail import EmailMultiAlternatives
import json
from django.http import JsonResponse
from .models import *
from WebSite.api import award_service
from WebSite.api import member_service


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
	data = {
		'state': request.POST['message'] + "<br>" + request.POST['email']
	}
	return JsonResponse(data)


def send_join_form(request):
	data = {
		'state':
			request.POST['names'] + "<br>" + request.POST['surnames'] +
			"<br>" + request.POST['email'] + "<br>" + request.POST['major'] +
			"<br>" + request.POST['reason']
	}
	return JsonResponse(data)


def contact_us(request):
	if request.method == 'POST':
		message = request.POST['message']
		email = request.POST['email']
		subject, from_email, to = \
			'Contact Us Form', 'acm@javeriana.edu.co', 'acm@javeriana.edu.co'
		# TODO: Generate function html from template and pass data
		html_content = \
			'<p>This is an <strong>ultimate2</strong> message.</p> {}'\
			.format(message)
		msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
		msg.content_subtype = "html"
		msg.send()

		subject = 'Contact Us Form'
		from_email = 'acm@javeriana.edu.co'
		to = email
		html_content = '<p>This is an <strong>ultimate3</strong> message.</p>'
		msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
		msg.content_subtype = "html"
		msg.send()
		return redirect('index')
	else:
		return render(request, 'index.html')


def page_not_found(request):
	return render(request, '404.html')
