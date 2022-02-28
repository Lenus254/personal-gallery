from pyexpat import model
from django.db import models
# from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
    def update_location(self, name): 
        self.name=name
        self.save   
        
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations    
        
        
        
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    def update_category(self, name): 
        self.name=name
        self.save     
        
        
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    # image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    description = models.TextField()
    # author = models.CharField(max_length=40, default='admin')
    # date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  
    
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()      
        
    def update_image(self,image, name, description, category, location): 
        self.image=image
        self.name=name
        self.description=description
        self.category=category
        self.location=location
        self.save      
        
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image 
    
    
    @classmethod
    def search_by_category(cl, category):
        images = cls.objects.filter(category__name =category)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
