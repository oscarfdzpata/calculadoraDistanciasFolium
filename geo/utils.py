from django.contrib.gis.geoip2 import GeoIP2


#Helper functions
def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip= x_forwarded_for.split(',')[0]
    else:
        ip= request.META.get('REMOTE_ADDR')
    return ip 

def get_geo(ip):
    g= GeoIP2()
    country = g.country(ip)
    city= g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon


def get_center_coordinates(latA, lonA, latB=None, lonB=None):
    cord= (latA, lonA)
    if latB:
        cord = [(latA+latB)/2, (lonA+lonB)/2]
    return cord

def get_zoom(distance):
    if distance <= 0.5:
        print("\n Distance Menor de 0,5", distance )
        return 16
    elif distance <= 10:
        print("\n Distance Menor de 10", distance )
        return 15
    elif distance <=100:
        print("\n Distance Menor de 100", distance )
        return 8        
    elif distance >100 and distance <=5000:
        print("\n Distance Mayor de 100 y  Menor de 5000", distance )
        return 4
    else:
        print("\n Distance Mayor de 5000", distance )
        return 2