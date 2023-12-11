from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import grade_list
from django import forms
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

def student_answer(request):
    my_students = grade_list.objects.all()
    template = loader.get_template('student_answer.html')
    context = {
        'Grades': my_students,
    }
    return HttpResponse(template.render(context, request))

def student_course(request):
    my_students = grade_list.objects.all()
    template = loader.get_template('student_course.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))


def chinese_grade_manage(request):
    my_students = grade_list.objects.all()
    template = loader.get_template('chinese_course.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))

def english_grade_manage(request):
    my_students = grade_list.objects.all()
    template = loader.get_template('english_course.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))

def math_grade_manage(request):
    my_students = grade_list.objects.all()
    template = loader.get_template('math_course.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))

def science_grade_manage(request):
    my_students = grade_list.objects.all()
    template = loader.get_template('science_course.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))

class StudentForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(label='Your Name', max_length=100)
    CHINESE = forms.IntegerField(label='國文')
    英文 = forms.IntegerField(label='英文')
    數學 = forms.IntegerField(label='數學')
    理化 = forms.IntegerField(label='理化') 
    

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = grade_list
        fields = '__all__'

def student_new(request):
    # Handle form submission
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data (you can save it to the database or perform other actions)
            # For now, just print the form data            
            student_instance = Student.objects.create(name=request.POST.get('name', ''))            
            course_instance = grade_list.objects.create(student=student_instance)   
            course_instance.國文 = request.POST.get('CHINESE', '')
            course_instance.英文 = request.POST.get('英文', '')
            course_instance.數學 = request.POST.get('數學', '')
            course_instance.理化 = request.POST.get('理化', '')
            student_instance.save()         
            course_instance.save()
            print(form.cleaned_data)
            # Redirect to a new URL:
            return redirect('student')
        
    else:
        # Display the form for the first time
        form = StudentForm()

    # Render the HTML template with the form
    return render(request, 'student_new_template.html', {'form': form})


def student_delete(request,record_id):
    # Get the record from the database
    record = get_object_or_404(grade_list, id=record_id)
    # Delete the record
    record.delete()    
    return redirect('student')

def student_update(request,record_id):
    # Get the record from the database
    record = get_object_or_404(grade_list, id=record_id)

    if request.method == 'POST':
        # Update the record from post data
        form = StudentModelForm(request.POST, instance=record)
        if form.is_valid():            
            #update the record to the database
            form.save()
            return redirect('student')  # Redirect to another URL after updating
    else:
        form = StudentModelForm(instance=record)

    return render(request, 'student_update_template.html', {'form': form, 'record': record})

