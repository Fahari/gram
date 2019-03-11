from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.photo= Image(name = 'black',caption ='black man')

    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Image))
