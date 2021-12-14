from django.db import models

# Create your models here.
class BikeLocation(models.Model):
    """
    Class to represent a c Bike location.
    """
    id = models.UUIDField(primary_key=True, null=False, editable=False)
    harvestTime = models.DateTimeField(null=True)
    stationID = models.IntegerField(null=True)
    availableBikeStands = models.IntegerField(null=True)
    bikeStands = models.IntegerField(null=True)
    availableBikes = models.IntegerField(null=True)
    banking = models.BooleanField(null=True)
    bonus = models.BooleanField(null=True)
    lastUpdate = models.DateTimeField(null=True)
    status = models.TextField(max_length=10, null=True)
    address = models.TextField(max_length=50, null=True)
    name = models.TextField(max_length=50, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
