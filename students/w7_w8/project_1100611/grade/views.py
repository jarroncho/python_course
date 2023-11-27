from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import grade_list

# Create your views here.

'''
def student(request):
    my_students = Student.objects.all().values()
    template = loader.get_template('student.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))
    '''

def grade(request):
    my_Grades = grade_list.objects.all()
    template = loader.get_template('student.html')
    context = {
        'Grades': my_Grades,
    }
    return HttpResponse(template.render(context, request))

