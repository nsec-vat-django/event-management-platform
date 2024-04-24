from django.urls import path
from . import views

urlpatterns = [
    path("", views.events, name="events"),
    path("add/", views.add_event, name="add_event"),
    path("past/", views.past_events, name="past_events"),
    path("event/<int:event_id>/", views.view_event, name="view_event"),
]
