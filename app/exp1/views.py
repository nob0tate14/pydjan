import django
from django.http.response import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('exp1/index.html')
    # return HttpResponse("Hello, world. You're at the example 1 index.")

    context = {
        'd_p': django.__path__,
    }
    return HttpResponse(template.render(context, request))
