from django.test import TestCase

from .models import Image, Category, Location


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Mara')
        self.location.save_location()

        self.category = Category(name='travel')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location,
                                category=self.category)
        
        
def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)
        
def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)
        
def test_search_image_by_category(self):
        category = 'travel'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()        
        
        
def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)
        
def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)                
        