from django.shortcuts import render
from WebSite.models import *

def index(request):
    return render(request, 'index.html')
