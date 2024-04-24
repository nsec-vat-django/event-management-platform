from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the events index.")