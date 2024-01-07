from django.urls import path

from . import views

urlpatterns = [
    path('grade/', views.student, name='grade'),
]
#控制網址
