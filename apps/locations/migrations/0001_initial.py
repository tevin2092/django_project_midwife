# Generated by Django 5.0.6 on 2024-07-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "location_id",
                    models.CharField(max_length=3, primary_key=True, serialize=False),
                ),
                ("location_name", models.CharField(max_length=50)),
            ],
        ),
    ]
