from django.shortcuts import get_object_or_404, render, redirect
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


def create_event(request):
    if request.method == "POST":
        # fetch data
        emp_name = request.POST.get("title")
        emp_description = request.POST.get("description")
        emp_date = request.POST.get("date")
        emp_location = request.POST.get("location")

        # create model object and set the data
        e = Event()
        e.title = emp_name
        e.description = emp_description
        e.date = emp_date
        e.location = emp_location

        # saving the data in database
        e.save()

        return redirect("/events/")
    return render(request, "events/add_events.html", {})
