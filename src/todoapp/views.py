from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
#jwt
import jwt
from rest_framework_jwt.utils import jwt_payload_handler


def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")

@api_view(['POST'])
def register(request):
    body = request.data
    email = body['email']

    user_exists = User.objects.get(email=email)
    if user_exists:
        return HttpResponse('Email already exists...', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        first_name = body['firstName']
        last_name = body['lastName']
        password = body['password']

        User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
        return HttpResponse('Created')
    except Exception:
        return HttpResponse('Error...')


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
 
    try:
        email = request.data['email']
        password = request.data['password']
 
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
 
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)