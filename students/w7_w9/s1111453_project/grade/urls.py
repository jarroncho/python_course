from django.urls import path
from . import views

urlpatterns = [    
    path('student/', views.student, name='grade'),
    path('student_course/', views.student_course, name='student_course'), 
    path('student/new', views.student_new, name='student_new_view'),
    # path('student/new_answser', views.student_new_answer, name='student_new_view_answer'),
    path('student/delete/<int:record_id>/', views.student_delete, name='student_delete_view'),
    path('student/update/<int:record_id>/', views.student_update, name='student_update_view'),
]