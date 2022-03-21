from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    data={
        "users":[{"name":"zack"},{"name":"zack"},]
    }
    return JsonResponse(data)