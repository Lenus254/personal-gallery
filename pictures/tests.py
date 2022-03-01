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