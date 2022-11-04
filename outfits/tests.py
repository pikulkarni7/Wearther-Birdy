from django.test import TestCase
import json
from .models import Product, Category
# Create your tests here.
class GarmentTest(TestCase):
    def setUp(self):
        upperwear = Category.objects.create(name='upperwear')
        bottomwear = Category.objects.create(name='bottomwear')
        
        tshirt = Category.objects.create(name='tshirt',parent=upperwear)
        jacket = Category.objects.create(name='jacket',parent=upperwear)
        jeans = Category.objects.create(name='jeans',parent=bottomwear)        
        chinos = Category.objects.create(name='chinos',parent=bottomwear)
        
        product1 = Product.objects.create(
            brand='Levis',
            model='J150',
            category=jeans,
            picture='blah',
            weather_value=4
        )
        
        product2 = Product.objects.create(
            brand='Levis',
            model='S200',
            category=jacket,
            picture='blah',
            weather_value=6
        )
        
        product3 = Product.objects.create(
            brand='Levis',
            model='J250',
            category=jeans,
            picture='blah',
            weather_value=5
        )
        
        product3 = Product.objects.create(
            brand='Levis',
            model='J350',
            category=jeans,
            picture='blah',
            weather_value=6
        )
        
    def test_product_search(self):
        
        bottomwear = Category.objects.filter(name='bottomwear')
        print(bottomwear)
        bottoms = Category.objects.filter(parent__in=bottomwear)
        print(bottoms)
        products=Product.objects.filter(category__in=bottoms)
        print((products))     
        assert 1==1
        
