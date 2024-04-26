from django.urls import path
from events import views

urlpatterns = [
    path("", views.events, name="events"),
    path("add/", views.add_events, name="add_events"),
    path("past/", views.past_events, name="past_events"),
    path("view/<int:event_id>/", views.view_events, name="view_events"),
<<<<<<< HEAD
    path("cancel/<int:event_id>/", views.cancel_event, name="cancel_events"),
    path('my_events/', views.my_events, name='my_events'),
=======
    path("edit/<int:event_id>/", views.edit_events, name="edit_events"),
    path("cancel/<int:event_id>/", views.cancel_events, name="cancel_events"),
>>>>>>> 909812f7792c34c7d028697c7a575f158c3e9b1d
]
