import django
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from exp1.components import chart_sample


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the example 1 index.")
    return render(request, 'exp1/index.html')


def page1(request):
    template = loader.get_template('exp1/page1.html')
    context = {
        'context': "this is context.",
    }
    return HttpResponse(template.render(context, request))


def chart(request):
    print("chart")
    r = chart_sample.get_data("1980/1999")
    r2 = chart_sample.get_data("2020/2039")
    # template = loader.get_template('exp1/page1.html')
    # return HttpResponse(template.render(None, request))
    context = {
        'data1': r,
        'data2': r2,
    }
    return render(request, 'exp1/chart_sample.html', context)
