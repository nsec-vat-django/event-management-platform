from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from events.models import Event


# Create your views here.
def events(request):
    # events = Event.objects.all()
    events = Event.objects.filter(date__gte=timezone.now())
    context = {"events": events}
    return render(request, "events/events.html", context)


def past_events(request):
    events = Event.objects.filter(date__lt=timezone.now())
    context = {"events": events}
    return render(request, "events/past_events.html", context)


def add_events(request):
    return render(request, "events/add_events.html")


def view_events(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/view_events.html", {"event": event})
