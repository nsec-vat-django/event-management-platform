from django.shortcuts import render
from .models import Event


# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "events/events.html", context)


def add_event(request):
    return render(request, "events/add_events.html")

