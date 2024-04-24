from django.http import Http404
from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    try:
        events = Event.objects.all()
        context = {"events": events}
        return render(request, "events/index.html", context)
    except Event.DoesNotExist:
        raise Http404("No events found")