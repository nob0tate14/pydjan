import django
from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the example 1 index.")
    template = loader.get_template('exp1/index.html')
    context = {
        'd_p': django.__path__,
    }
    return HttpResponse(template.render(context, request))


def page1(request):
    # template = loader.get_template('exp1/page1.html')
    # return HttpResponse(template.render(None, request))
    return render(request, 'exp1/page1.html')
