from django.http import JsonResponse
from django.shortcuts import render

from projects.models import Project

# Create your views here.
def index(req):
    data = list(Project.objects.values())
    return JsonResponse(data, safe=False)