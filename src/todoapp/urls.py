from django.urls import path
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('me', views.UserViewSet.as_view({'get': 'get_user_data'}), name='users'),
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.authenticate_user, name='login'),
    path('createitem', views.TodoViewSet.as_view({'post': 'create_item'}), name='createitem'),
    path(r'delete/<id>', views.delete),
    path(r'update/<id>', views.update),
    path(r'changeCompleted/<id>', views.changeCompleted),
    path('todos', views.TodoViewSet.as_view({'get': 'get_items'}), name='todos')
]