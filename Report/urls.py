from django.conf.urls import include, url
from django.urls import path
from .views import HomePageView, county_datasets, point_datasets

print('-----Report/urls----')

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('county_data/', county_datasets, name='county'),
    path('incidence_data/', point_datasets, name='incidences')
]