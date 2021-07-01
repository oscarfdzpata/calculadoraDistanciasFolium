from django.test import TestCase

# Create your tests here.

from . import views
from . import utils

class TestViews(TestCase):

    def setUp(self):
        ''' Se ejecuta antes de los test'''



    def test_simple(self):
        result = utils.get_zoom(0.5)
        '''
        self.assertEqual(VALOR OBTENIDO, VALOR ESPERADO)
        '''
        self.assertEqual(result, 16)
    def test_simple2(self):
        result = utils.get_zoom(10)
        self.assertEqual(result, 15)
    def test_simple3(self):
        result = utils.get_zoom(100)
        self.assertEqual(result, 8)
    def test_simple4(self):
        result = utils.get_zoom(5001)
        self.assertEqual(result, 2)



    