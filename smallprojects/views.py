from django.shortcuts import render
from .models import SmallProjects

def allprojects(request):
    smallprojects = SmallProjects.objects
    return render(request, 'project/allprojects.html', {'smallprojects':smallprojects})
