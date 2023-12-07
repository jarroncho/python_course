from django.shortcuts import render


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def simple_hello(request):
    return HttpResponse("Hello world!")

def template_hello(request):
    template = loader.get_template('first_page.html')
    return HttpResponse(template.render())
