from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.generics import RetrieveAPIView
from src.todoapp.serializers import CreateUserSerializer, UserSerializer
from rest_framework import viewsets, mixins
from src.todoapp.permissions import IsUserOrReadOnly
from rest_framework.decorators import action
#jwt
import jwt
from rest_framework_jwt.utils import jwt_payload_handler

def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")

@api_view(['POST'])
def register(request):
    body = request.data
    email = body['email']

    try:
        user_exists = User.objects.get(email=email)
        if user_exists:
            return HttpResponse('Email already exists...', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception:
        pass
    
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


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates, Updates and Retrieves - User Accounts
    """
    queryset = User.objects.all()
    serializers = {
        'default': UserSerializer,
        'create': CreateUserSerializer
    }
    permissions = {
        'default': (IsUserOrReadOnly,),
        'create': (AllowAny,)
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.permissions['default'])
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='me', url_name='me')
    def get_user_data(self, instance):
        try:
            return Response(UserSerializer(self.request.user, context={'request': self.request}).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Wrong auth token' + e}, status=status.HTTP_400_BAD_REQUEST)