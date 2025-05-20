from django.db import models

class ProductManager(models.Manager):        
    def available(self):
        return self.filter(available=True)
    
    def featured(self):
        return self.available().filter(featured=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()  # The default manager
    items = ProductManager()    # Our custom manager
    
    def __str__(self):
        return self.name