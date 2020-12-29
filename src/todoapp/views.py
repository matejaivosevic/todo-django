from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from .models import User
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")

@api_view(['POST'])
def register(request):
    body = request.data
    
    try:
        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        password = body['password']

        User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
        return HttpResponse('Created')
    except Exception:
        return HttpResponse('Error...')
