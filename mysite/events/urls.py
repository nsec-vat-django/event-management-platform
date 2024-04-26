from django.urls import path
from events import views

urlpatterns = [
    path("", views.events, name="events"),
    path("add/", views.add_events, name="add_events"),
    path("past/", views.past_events, name="past_events"),
    path("view/<int:event_id>/", views.view_events, name="view_events"),
    path("create-event/",views.create_event),
]
