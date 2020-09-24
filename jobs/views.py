from django.shortcuts import render
from .models import Job
from completedjobs.models import CompletedJob

def home(request):
    jobs = Job.objects
    completedjobs = CompletedJob.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'completedjobs':completedjobs})
