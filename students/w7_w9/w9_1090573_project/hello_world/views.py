# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def simple_hello(request):
    return HttpResponse("Simple Hello world!")


def template_hello(requset):
    template = loader.get_template('first_page.html')
    return HttpResponse(template.render())