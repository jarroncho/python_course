from django.urls import path
from . import views

urlpatterns = [    
    #path('student/', views.student, name='grade'),
    path('student/', views.grade, name='student'),
    path('student_answer/', views.student_answer, name='student_answer'),   
    #w9 
    path('student_course/', views.student_course, name='student_course'), 
    path('student/chinese', views.chinese_grade_manage, name='chinese_course'),
    path('student/english', views.english_grade_manage, name='english_course'), 
    path('student/math', views.math_grade_manage, name='math_course'), 
    path('student/science', views.science_grade_manage, name='science_course'), 
    path('student/new', views.student_new, name='student_new_view'),
    path('student/delete/<int:record_id>/', views.student_delete, name='student_delete_view'),
    path('student/update/<int:record_id>/', views.student_update, name='student_update_view'),
]