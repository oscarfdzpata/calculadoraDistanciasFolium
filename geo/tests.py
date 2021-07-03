from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse


from django.test import Client

# Create your tests here.

from . import views
from . import utils
from .models import Measurement


class TestUtils_getZoom(TestCase):

    def setUp(self):
        #Se ejecuta antes de los test
        print("\n Comienzo de los test")

    def test_getZoom1(self):
        result = utils.get_zoom(0.5)        
        #self.assertEqual(VALOR OBTENIDO, VALOR ESPERADO)        
        self.assertEqual(result, 16)
    def test_getZoom2(self):
        result = utils.get_zoom(10)
        self.assertEqual(result, 15)
    def test_getZoom3(self):
        result = utils.get_zoom(100)
        self.assertEqual(result, 8)
    def test_getZoom4(self):
        result = utils.get_zoom(5001)
        self.assertEqual(result, 2)


'''
class TestHTTP(SimpleTestCase):

    def test_status_ok(self):
        #response = self.client.get("/")
        c= Client()
        response = c.get("/")
        self.assertEquals(response.status_code, 200)
'''

    

#class HomePageTests(SimpleTestCase):  Si hay acceso a BBDD hay que poner TestCase
#https://stackoverflow.com/questions/57007022/assertion-error-while-testing-django-views
class TestsMainPage(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)        
    
    
    def test_home_url_name(self):
        response= self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response= self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'measurement/main.html')


class TestsIndexPage(TestCase):
    def test_index_status_code(self):
           
        response = self.client.get('/index/')
        self.assertEquals(response.status_code, 200)
    
    def test_index_url_name(self):
        response= self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)


class TestModelMeasurement(TestCase):
    @classmethod
    def setUp(cls):

        location= 'La rioja, España'
        destination= 'Madrid, España'
        distance= 400.00
        Measurement.objects.create(location=location, destination=destination, distance=distance)
    
    def test_distance(self):
        measurement= Measurement.objects.get(id=1)
        expected_measurement_distance = measurement.distance
        self.assertEquals(expected_measurement_distance, 400.00)
    
    def test_measurement_view_home(self):
        response= self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'measurement/main.html')
        self.assertContains(response,'400.00')   #Comprobamos que dentro del response hay incluido el texto 400.00 que es un campo del registro creado en la prueba.



    
