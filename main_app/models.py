from django.db import models

# Create your models here.

# Create your models here.
class Boat(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    length = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.make 
    
