from django.db import models
from clients.models import Client
from midwives.models import Midwife


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=20, primary_key=True)
    midwife = models.ForeignKey(Midwife, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.appointment_id} - {self.date} {self.time}"
