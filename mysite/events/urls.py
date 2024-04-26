from django.urls import path
from events import views

urlpatterns = [
    path("", views.events, name="events"),
    path("add/", views.add_events, name="add_events"),
    path("past/", views.past_events, name="past_events"),
    path("view/<int:event_id>/", views.view_events, name="view_events"),
    path("cancel/<int:event_id>/", views.cancel_event, name="cancel_events"),
    path('my_events/', views.my_events, name='my_events'),
]
