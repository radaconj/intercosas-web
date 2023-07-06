from django.shortcuts import render
from .models import Project


def home(request):
    projects_list = Project.objects.all()

    return render(request, 'home.html', {'projects': projects_list})
