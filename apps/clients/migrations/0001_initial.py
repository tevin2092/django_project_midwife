# Generated by Django 5.0.6 on 2024-07-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("client_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=100)),
                ("address", models.CharField(max_length=100)),
            ],
        ),
    ]
