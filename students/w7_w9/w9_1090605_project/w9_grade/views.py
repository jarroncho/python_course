from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student, Course
from django import forms

# Create your views here.
def student(request):
    my_students = Student.objects.all().values()
    template = loader.get_template('student.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))

# create /delete 
def student_course(request):
    my_students = Student.objects.all().values()
    template = loader.get_template('student_course.html')
    context = {
        'Students': my_students,
    }
    return HttpResponse(template.render(context, request))


class StudentForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(label='Your Name', max_length=100)
    

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

def student_new(request):
    # Handle form submission
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data (you can save it to the database or perform other actions)
            # For now, just print the form data            
            student_instance = Student.objects.create(name=request.POST.get('name', ''))            
            course_instance = Course.objects.create(student=student_instance)            
            student_instance.save()
            print(form.cleaned_data)
            # Redirect to a new URL:
            return redirect('student_course')
        
    else:
        # Display the form for the first time
        form = StudentForm()

    # Render the HTML template with the form
    return render(request, 'student_new_template.html', {'form': form})


def student_delete(request,record_id):
    # Get the record from the database
    record = get_object_or_404(Student, id=record_id)
    # Delete the record
    record.delete()    
    return redirect('student_course')

def student_update(request,record_id):
    # Get the record from the database
    record = get_object_or_404(Student, id=record_id)

    if request.method == 'POST':
        # Update the record from post data
        form = StudentModelForm(request.POST, instance=record)
        if form.is_valid():            
            #update the record to the database
            form.save()
            return redirect('student_course')  # Redirect to another URL after updating
    else:
        form = StudentModelForm(instance=record)

    return render(request, 'student_update_template.html', {'form': form, 'record': record})

def simple_hello(request):
    return HttpResponse("Simple Hello world!")


def template_hello(request):
    template = loader.get_template('first_page.html')
    return HttpResponse(template.render())