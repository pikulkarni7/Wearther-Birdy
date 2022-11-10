from django.db import models

from authentication.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name
        
    
class Product(models.Model):  
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shade = models.CharField(max_length=20)
    picture = models.CharField(max_length=250)
    weather_value = models.IntegerField()


class Formality(models.Model):
    F_VALUES = (
        ('F', 'FORMAL'),
        ('S', 'SEMI-FORMAL'),
        ('C', 'CASUAL'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(choices=F_VALUES, max_length=1)
    

class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    
    

