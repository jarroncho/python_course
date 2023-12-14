from django.urls import path
from . import views

urlpatterns = [
    # path('simple/', views.simple_hello, name='hello_world'),
    # path('template/', views.template_hello, name='hello_world'),
    path('student/', views.student, name='student'),  
    #w9 
    path('student_course/', views.student_course, name='student_course'), 
    path('student/new', views.student_new, name='student_new_view'),
    path('student/delete/<int:record_id>/', views.student_delete, name='student_delete_view'),
    path('student/update/<int:record_id>/', views.student_update, name='student_update_view'),
]