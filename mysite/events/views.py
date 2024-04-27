from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib import messages
from events.models import Event, Participant
from django.contrib.auth.decorators import login_required


def events(request):
    # events = Event.objects.all()
    events = Event.objects.filter(date__gte=timezone.now()).order_by("date")
    context = {"events": events}
    return render(request, "events/events.html", context)


def past_events(request):
    events = Event.objects.filter(date__lt=timezone.now()).order_by("date")
    context = {"events": events}
    return render(request, "events/past_events.html", context)


def view_events(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(
        request, "events/view_events.html", {"event": event, "now": timezone.now()}
    )


def register_events(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        participant, created = Participant.objects.get_or_create(name=name, email=email)
        if event.participants.count() >= event.max_participants:
            messages.warning(request, "This Event is Full!")
        elif event.participants.filter(id=participant.id).exists():
            messages.warning(request, "You Are Already Registered For This Event!")
        else:
            event.participants.add(participant)
            event.num_participants += 1
            event.save()
            messages.success(request, "Registration Successful!")
        return redirect("events")
    return render(request, "events/register_events.html", {"event": event})


def add_events(request):
    if request.method == "POST":
        event = Event()
        event.title = request.POST.get("title")
        event.description = request.POST.get("description")
        event.date = request.POST.get("date") + " " + request.POST.get("time")
        event.location = request.POST.get("location")
        event.max_participants = request.POST.get("max_participants")
        event.user = request.user
        event.save()
        messages.success(request, "Event Creation Successful!")
        return redirect("events")
    return render(request, "events/add_events.html", {})


def edit_events(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        event.title = request.POST.get("title")
        event.description = request.POST.get("description")
        event.date = request.POST.get("date") + " " + request.POST.get("time")
        event.location = request.POST.get("location")
        event.max_participants = request.POST.get("max_participants")
        event.save()
        messages.success(request, "Edit Event Successful!")
        return redirect("events")
    else:
        context = {"event": event}
    return render(request, "events/edit_events.html", context)


def cancel_events(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, "Event Deletion Successful!")
    return redirect("events")


@login_required
def my_events(request):
    events = Event.objects.filter(user=request.user).order_by("date")
    username = request.user.username
    return render(
        request, "events/my_events.html", {"events": events, "username": username}
    )
