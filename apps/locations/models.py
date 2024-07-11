from django.db import models

class Location(models.Model):
    location_id = models.CharField(max_length=3, primary_key=True)
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name
