from django.urls import path
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('me', views.UserViewSet.as_view({'get': 'get_user_data'}), name='users'),
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.authenticate_user, name='login')

]