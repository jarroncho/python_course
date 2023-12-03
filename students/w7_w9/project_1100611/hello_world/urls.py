from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple_hello, name='hello_world'),
    path('template/', views.template_hello, name='hello_world'),
]
