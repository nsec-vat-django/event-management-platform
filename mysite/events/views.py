from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from events.models import Event
from django.contrib.auth.decorators import login_required


def events(request):
    # events = Event.objects.all()
    events = Event.objects.filter(date__gte=timezone.now())
    context = {"events": events}
    return render(request, "events/events.html", context)


def past_events(request):
    events = Event.objects.filter(date__lt=timezone.now())
    context = {"events": events}
    return render(request, "events/past_events.html", context)


def view_events(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/view_events.html", {"event": event})


def add_events(request):
    if request.method == "POST":
        # fetch data
        event_title = request.POST.get("title")
        event_description = request.POST.get("description")
        event_date = request.POST.get("date")
        event_location = request.POST.get("location")

        # create model object and set the data
        event = Event()
        event.title = event_title
        event.description = event_description
        event.date = event_date
        event.location = event_location

        # saving the data in database
        event.save()

        return redirect("events")
    return render(request, "events/add_events.html", {})


def cancel_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect("events")

@login_required
def my_events(request):
    events = Event.objects.filter(user=request.user)
    username = request.user.username
    return render(request, 'events/my_events.html', {'events': events, 'username': username})