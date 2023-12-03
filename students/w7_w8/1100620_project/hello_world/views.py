# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def simple_hello(request):
    return HttpResponse("Simple Sunny Hello world!")


def template_hello(request):
    template = loader.get_template('first_page.html')
    return HttpResponse(template.render())
