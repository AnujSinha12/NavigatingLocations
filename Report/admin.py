from django.contrib import admin
from .models import Incidences, Counties
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
@admin.register(Incidences)
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

@admin.register(Counties)
class CountiesAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')



