from django.shortcuts import render
from .models import CompletedJob

def home(request):
    completedjobs = CompletedJob.objects
    return render(request, 'jobs/home.html', {'completedjobs':completedjobs})
