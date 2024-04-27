from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    max_participants = models.IntegerField(default=5)
    num_participants = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    events = models.ManyToManyField(Event, related_name="participants")

    def __str__(self):
        return self.name
