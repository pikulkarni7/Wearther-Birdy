from django.test import TestCase
import json
from .models import Product, Type
from django.core.serializers import serialize
# Create your tests here.
class GarmentTest(TestCase):
    def setUp(self):
        upperwear = Type.objects.create(name='upperwear')
        bottomwear = Type.objects.create(name='bottomwear')
        
        tshirt = Type.objects.create(name='tshirt',parent=upperwear)
        jacket = Type.objects.create(name='jacket',parent=upperwear)
        jeans = Type.objects.create(name='jeans',parent=bottomwear)        
        chinos = Type.objects.create(name='chinos',parent=bottomwear)
        
        short_chinos = Type.objects.create(name='short_chinos', parent=chinos)
        
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
        
        product4 = Product.objects.create(
            brand='Spyder',
            model='C550',
            category=chinos,
            picture='blah',
            weather_value=2
        )
        
        product5 = Product.objects.create(
            brand='Banana',
            model='C150',
            category=short_chinos,
            picture='blah',
            weather_value=2
        )
        
    def test_product_search(self):
        
     
        queryset = Type.objects.get(name='jeans')

        if not queryset.is_leaf_node():
            children = queryset.get_children()
        
            while not children[0].is_leaf_node():
                children = children[0].get_children()

            children = children[0].get_siblings(include_self=True)
            print(Product.objects.filter(category__in=children).values())
        else:
            print(Product.objects.filter(category__in=[queryset]).values()) 
    
        assert 1==1
        
