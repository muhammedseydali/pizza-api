from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .import views

urlpatterns = [
    path('', views.hello),
    path('signup/', views.UserCreateView.as_view(), name='signup'),

]
