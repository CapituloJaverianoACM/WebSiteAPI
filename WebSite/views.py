from WebSite.models import *
from django.shortcuts import render, redirect
from datetime import datetime, date
from django.core.mail import EmailMultiAlternatives

def index(request):
	awards = Award.objects.order_by('-date')
	recentActivities = []
	orderToFuture = Activity.objects.exclude(date__lt = date.today()).order_by('date')
	for activity in orderToFuture:
		recentActivities.append(activity)
		if len(recentActivities) == 3:
			break
	orderToPast = Activity.objects.exclude(date__gt = date.today()).order_by('-date')
	for activity in orderToPast:
		recentActivities.append(activity)
		if len(recentActivities) == 6:
			break
	ourProjects = []
	projects = Project.objects.order_by('-dateEnd')
	for project in projects:
		if len(ourProjects) == 5:
			break;
		ourProjects.append(project)
	context = {
		'awards' : awards,
		'recentActivities' : recentActivities,
		'ourProjects' : ourProjects
	}
	return render(request, 'index.html', context)

def staff(request):
	return render(request, 'staff.html')

def contest(request):
	return render(request, 'contests.html')

def activities(request):
	return render(request, 'activities.html')

def activityDetail(request, idActivity):
	return render(request, 'index.html')

def projects(request):
	return render(request, 'projects.html')

def projectDetail(request, idProject):
	return render(request, 'index.html')

def tutorials(request):
	return render(request, 'tutorials.html')

def tutorialDetail(request, idTutorial):
	return render(request, 'index.html')

def contactUs(request):
	if request.method == 'POST':
		message = request.POST['message']
		email = request.POST['email']
		subject, from_email, to = 'Contact Us Form', 'acm@javeriana.edu.co', 'acm@javeriana.edu.co'
		html_content = '<p>This is an <strong>ultimate2</strong> message.</p>'
		msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
		msg.content_subtype = "html"
		msg.send()

		subject, from_email, to = 'Contact Us Form', 'acm@javeriana.edu.co', email
		html_content = '<p>This is an <strong>ultimate3</strong> message.</p>'
		msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
		msg.content_subtype = "html"
		msg.send()
		return redirect('index')
	else:
		return render(request, 'index.html')
