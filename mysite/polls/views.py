from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    #template = loader.get_template("polls/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(template.render())
