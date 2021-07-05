from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Measurement

from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from .utils import get_geo,get_center_coordinates, get_zoom, get_ip_address

import folium
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def calculate_distance_view(request):
    #obj= get_object_or_404(Measurement, id=1)
    distance= None
    obj=Measurement.objects.last()
    form= MeasurementModelForm(request.POST or None)
    geolocator= Nominatim(user_agent='measurements')

    location_= None
    destination_=None

    
    ''' Controlo el location desde la ip de origen
    ip= '90.170.170.12'
    #obtenemos la ip
    ip_= get_ip_address(request)
    print("\n La ip de origen es:" , ip_)
    country, city, lat, lon = get_geo(ip)
    print('location country', country)
    print('location city', city)
    print('location lat', lat)
    print('location lon', lon)        
    location= geolocator.geocode(city)
    print("###", location)
    '''



    #Pongo el valor de origen por defecto en Obispo Lepe ####################################################
    origen_='obispo lepe, logroño'
    search_location = None
    if request.GET.get('search_location'):
        search_location = request.GET.get('search_location')
        print("\n Search Location:" , search_location)
        origen_=search_location
    try:
        origen=geolocator.geocode(origen_)
        location= origen       
        #origen cordenadas
        if location is not  None:
            o_lat=origen.latitude
            o_lon=origen.longitude
        else:
            search_location = None
            origen_='Logroño'
            origen=geolocator.geocode(origen_)
            location= origen       
            #origen cordenadas
            o_lat=origen.latitude
            o_lon=origen.longitude

        pointO=(o_lat, o_lon)
        #initial folium map con Obispo Lepe
        #m= folium.Map(width=800, heigth=500, location=pointO)
        m= folium.Map(width="100%", heigth=500, id="mapa", location=get_center_coordinates(o_lat, o_lon), zoom_start=5)
        #location marker
        folium.Marker([o_lat, o_lon], tooltip='click aqui para ver mas', popup=origen,
                    icon=folium.Icon(color='purple')).add_to(m)
    except Exception as e:
        print("\n Ocurrio algun error, puede ser el location  ", e)

    


    if request.method=="GET" and request.GET.get('search_location') is  None:

        try:        
            last_measeure_save=Measurement.objects.all().last()
            destination_= last_measeure_save.destination
            destination=geolocator.geocode(destination_)
            #destination=destination_

            #destino cordenadas
            d_lat=destination.latitude
            print(destination.longitude)
            d_lon=destination.longitude

            #origen cordenadas desde el form
            location_=last_measeure_save.location
            location=geolocator.geocode(location_)
            #location=location_
        
            #origen cordenadas
            o_lat=location.latitude
            o_lon=location.longitude
            pointO = (o_lat, o_lon)


            pointB = (d_lat, d_lon)
            #calculo de distancias
            distance=round(geodesic(pointO,pointB).km,2)

            #folium map modification
            #m= folium.Map(width=800, heigth=500, location=pointO)
            m= folium.Map(width="100%", heigth=500, location=get_center_coordinates(o_lat, o_lon, d_lat, d_lon), zoom_start=get_zoom(distance)) #zoom_start=15
            #location marker
            folium.Marker([o_lat, o_lon], tooltip='click aqui para ver mas', popup=location, #popup=origen,
                    icon=folium.Icon(color='purple')).add_to(m)
            #destination marker
            folium.Marker([d_lat, d_lon], tooltip='click aqui para ver mas', popup=destination,
                    icon=folium.Icon(color='red', icon='cloud')).add_to(m)


            #Draw the line beetewn location and destination
            line= folium.PolyLine(locations=[pointO,pointB], weight=2, color='blue')
            m.add_child(line)

        except Exception as e:
            print("\n Ocurrio algun error, puede ser el location o el destination: ", e)



    if request.method=="POST":
        if form.is_valid():
            instance=form.save(commit=False)
            #instance.destination=form.cleaned_data.get('destination')
            destination_=form.cleaned_data.get('destination')  
            destination=destination_
                
            try:

      
                #destino cordenadas
                d_lat=destination.latitude
                d_lon=destination.longitude

                #origen cordenadas desde el form
                location_=form.cleaned_data.get('location')        
                location=location_

                #origen cordenadas
                o_lat=location.latitude
                o_lon=location.longitude
                pointO = (o_lat, o_lon)


                pointB = (d_lat, d_lon)
                #calculo de distancias
                distance=round(geodesic(pointO,pointB).km,2)

                #folium map modification
                #m= folium.Map(width=800, heigth=500, location=pointO)
                m= folium.Map(width="100%", heigth=500, location=get_center_coordinates(o_lat, o_lon, d_lat, d_lon), zoom_start=get_zoom(distance)) #zoom_start=15
                #location marker
                folium.Marker([o_lat, o_lon], tooltip='click aqui para ver mas', popup=location, #popup=origen,
                        icon=folium.Icon(color='purple')).add_to(m)
                #destination marker
                folium.Marker([d_lat, d_lon], tooltip='click aqui para ver mas', popup=destination,
                        icon=folium.Icon(color='red', icon='cloud')).add_to(m)


                #Draw the line beetewn location and destination
                line= folium.PolyLine(locations=[pointO,pointB], weight=2, color='blue')
                m.add_child(line)

                instance.destination=destination
                instance.location=location
                instance.distance= distance
                instance.save()
                obj=Measurement.objects.last()
            except Exception as e:
                print("\n Ocurrio algun error, puede ser el location o el destination: ", e)
        else:
            print("\n FORM ERRORs ", form.errors )

    obj_measurement= Measurement.objects.all().order_by('-id')[:5]



    m= m._repr_html_()

    

    context={
        'obj_measurements' : obj_measurement,
        'distance' : distance,
        'form': form,
        'map': m,
        'location': location_,
        'destination': destination_,
        'search_location' : search_location,
    }

    return render(request, 'measurement/main.html',context )