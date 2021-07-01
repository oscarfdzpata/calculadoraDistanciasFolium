from django import forms
from .models import Measurement

#Linrerias para validar el dato de entrada, que existe esa ubicacion
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo,get_center_coordinates, get_zoom, get_ip_address

import folium

class MeasurementModelForm(forms.ModelForm):


    class Meta:
        model= Measurement
        fields = ('location','destination',)
       

    def clean_destination(self):
        geolocator= Nominatim(user_agent='measurements')
        destination_= self.cleaned_data.get('destination')  
        destination=geolocator.geocode(destination_)       
        if destination is None:
            raise forms.ValidationError("La ubicacion de destino debe ser real")
        
        return destination


    def clean_location(self):
        geolocator= Nominatim(user_agent='measurements')
        location_= self.cleaned_data.get('location')
        location=geolocator.geocode(location_)
        if location is None:         
            raise forms.ValidationError("El origen debe ser una ubicacion real")

        return location

    '''
    def clean(self):
        geolocator= Nominatim(user_agent='measurements')
        destination_= self.cleaned_data.get('destination')
        destination=geolocator.geocode(destination_) 
        if destination is None:
            raise forms.ValidationError("La ubicacion de destino debe ser real")

        return self.cleaned_data
    '''

