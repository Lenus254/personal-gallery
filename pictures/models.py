from pyexpat import model
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
