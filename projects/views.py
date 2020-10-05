from django.shortcuts import render, get_object_or_404
from .models import Project
from smallprojects.models import SmallProjects

def allprojects(request):
    projects = Project.objects
    smallprojects = SmallProjects.objects
    return render(request, 'project/allprojects.html', {'projects':projects, 'smallprojects':smallprojects})


def detail(request, project_id):
    detailprojects = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/detail.html', {'projects':detailprojects})
