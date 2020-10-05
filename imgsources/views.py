from django.shortcuts import render
from .models import Imgsources


def imgSources(request):
    imgsources = Imgsources.objects
    return render(request, 'imgsource/imgSources.html', {'imgsources':imgsources})
