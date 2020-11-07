from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
##Getting models from current directory
from .models import Counties, Incidences

print('----Report/view---')

class HomePageView(TemplateView):
    template_name = 'index.html'

def county_datasets(request):
    print('____Report/views/county_datasets____')
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')

def point_datasets(request):
    print('____Report/views/point_datasets____')
    points = serialize('geojson', Incidences.objects.all())
    return HttpResponse(points, content_type='json')

