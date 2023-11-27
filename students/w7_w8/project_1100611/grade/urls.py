from django.urls import path
from . import views

urlpatterns = [    
    #path('student/', views.student, name='grade'),
    path('student/', views.grade, name='grade'),
]