from django.db import models

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name
