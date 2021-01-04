from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.authenticate_user, name='login'),
    path('me', views.UserProfileView.as_view(), name='profile'),

]