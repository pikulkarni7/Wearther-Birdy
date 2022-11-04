from mptt.models import MPTTModel, TreeForeignKey
from django.db import models

   
    
class Type(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('Type', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    category = models.ForeignKey(Type, on_delete=models.CASCADE)
    shade = models.CharField(max_length=10)
    picture = models.CharField(max_length=250)
    weather_value = models.PositiveIntegerField()


class Formality(models.Model):
    F_VALUES = (
        ('F', 'FORMAL'),
        ('S', 'SEMI-FORMAL'),
        ('C', 'CASUAL'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(choices=F_VALUES, max_length=1)
    


    
    

