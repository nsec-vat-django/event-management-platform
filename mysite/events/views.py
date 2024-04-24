from django.shortcuts import get_object_or_404, render
from .models import Event


# Create your views here.
def events(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "events/events.html", context)


def add_event(request):
    return render(request, "events/add_events.html")


def view_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/view_events.html", {"event": event})
