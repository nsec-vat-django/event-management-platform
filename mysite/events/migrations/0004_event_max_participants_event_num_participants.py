# Generated by Django 5.0.4 on 2024-04-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0003_participant"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="max_participants",
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name="event",
            name="num_participants",
            field=models.IntegerField(default=0),
        ),
    ]
