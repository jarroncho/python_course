# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from . import views

def simple_hello(request):
    return HttpResponse("YZU 校女籃好棒棒!!!")

def template_hello(request):
    template = loader.get_template('first_page.html')
    return HttpResponse(template.render())
