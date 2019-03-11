from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    #Testing instantiation
    def setUp(self):
        self.photo= Image(name = 'black',caption ='black man')

    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Image))

    # Testing Save Method
    def test_save_method(self):
        self.photo.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    def tearDown(self):
        Image.objects.all().delete()
