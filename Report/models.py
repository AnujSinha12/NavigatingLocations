from django.db import models
from django.contrib.gis.db import models
from datetime import datetime


print('---Report/models---')

# Create your models here.
class Incidences(models.Model):
    print('****Report/models/Incidences***')
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)


class Counties(models.Model):
    print('****Report/models/Counties***')
    counties = models.CharField(max_length=25, default='')
    codes = models.IntegerField(default=0)
    cty_code = models.CharField(max_length=24, default='')
    ##dis = models.IntegerField(default='NULL')
    geom = models.MultiPolygonField(srid=4326)
    ##time = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.counties

