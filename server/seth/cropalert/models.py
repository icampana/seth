from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return unicode(self.name)

class Plant(models.Model):
    name = models.CharField(max_length=250)
    subtype = models.CharField(max_length=250)

    def __unicode__(self):
        return unicode(self.name)

class Pest(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return unicode(self.name)


class PlantPestSusceptibility(models.Model):
    plant = models.ForeignKey("Plant")
    pest = models.ForeignKey("Pest")

    def __unicode__(self):
        return unicode(self.plant.name + "-" + self.pest.name )

class Pesticide(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return unicode(self.name)

class PestPlantPesticideRel(models.Model):
    plantpestsusceptibility = models.ForeignKey("PlantPestSusceptibility")
    pesticide = models.ForeignKey("Pesticide")

    def __unicode__(self):
        return unicode(self.plantpestsusceptibility.__unicode__() + "-" +self.pesticide.name)

class Crop(models.Model):
    AREAMEASUREMENTUNIT_CHOICES = (
        (0, 'Square Feet'),
        (1, 'Square Meter'),
        )
    name = models.CharField(max_length=250)
    coordinates = GeopositionField()
    plant = models.ForeignKey("Plant")
    areameasurement = models.DecimalField(max_digits=9,decimal_places=4)
    measurementunit = models.IntegerField(choices=AREAMEASUREMENTUNIT_CHOICES)
    planting_date = models.DateField()
    estimated_harvest_date = models.DateField()
    aprox_plant_number = models.IntegerField()
    harvested = models.BooleanField()
    grower = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.plant.name)

class PestIdentificacionRequest(models.Model):
    crop = models.ForeignKey("Crop")
    taken = models.DateField()
    picture = models.ImageField(upload_to='uploads')

    def __unicode__(self):
        return unicode(self.crop.name + str(self.taken))


class PestIdentification(models.Model):
    pestidentificacionrequest = models.ForeignKey("PestIdentificacionRequest")
    user = models.ForeignKey(User)
    pest = models.ForeignKey("Pest")

    def __unicode__(self):
        return unicode(self.crop.name)

