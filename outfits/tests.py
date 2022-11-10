from django.test import TestCase
import json
from .models import Product, Category
from .queries import get_products_by_category
from .omaster import compute_suggestions
from django.core.serializers import serialize


# Create your tests here.
class GarmentTest(TestCase):
    def setUp(self):
        
        bottomwear = Category.objects.create(name='bottomwear')
        women = Category.objects.create(name="women")
        top_required = Category.objects.create(name='top_required')
        top_optional_1 = Category.objects.create(name='top_optional_1')
        top_optional_2 = Category.objects.create(name='top_optional_2')
        
        # tshirt = Category.objects.create(name='tshirt',parent=upperwear)
        # jacket = Category.objects.create(name='jacket',parent=upperwear)
        # jeans = Category.objects.create(name='jeans',parent=bottomwear)        
        # chinos = Category.objects.create(name='chinos',parent=bottomwear)
        
        # short_chinos = Type.objects.create(name='short_chinos', parent=chinos)
        
        product1 = Product.objects.create(
            brand='Hollister',
            model='shorts',
            category=bottomwear,
            picture='blah',
            weather_value=1
        )
        
        product2 = Product.objects.create(
            brand='Levis',
            model='pants',
            category=bottomwear,
            picture='blah',
            weather_value=4
        )
        
        product3 = Product.objects.create(
            brand='ZARA',
            model='dress',
            category=women,
            picture='blah',
            weather_value=5
        )
        
        product4 = Product.objects.create(
            brand='Levis',
            model='ss-shirt',       #short-sleeve-shirt
            category=top_required,
            picture='blah',
            weather_value=1
        )
        
        product5 = Product.objects.create(
            brand='Spyder',
            model='ls_shirt',
            category=top_required,
            picture='blah',
            weather_value=3
        )
        
        product6 = Product.objects.create(
            brand='Banana',
            model='hoodie',
            category=top_optional_1,
            picture='blah',
            weather_value=5
        )
        
        product7 = Product.objects.create(
            brand='Banana',
            model='jacket',
            category=top_optional_1,
            picture='blah',
            weather_value=7
        )
        
        product8 = Product.objects.create(
            brand='Banana',
            model='sweater',
            category=top_optional_1,
            picture='blah',
            weather_value=9
        )
        
        product9 = Product.objects.create(
            brand='Banana',
            model='windbreaker',
            category=top_optional_2,
            picture='blah',
            weather_value=13
        )
        
        product10 = Product.objects.create(
            brand='Banana',
            model='coat',
            category=top_optional_2,
            picture='blah',
            weather_value=15
        )
        
        product11 = Product.objects.create(
            brand='Banana',
            model='down_jacket',
            category=top_optional_2,
            picture='blah',
            weather_value=17
        )
        
        
        
    def test_product_search(self):
        
     
        # queryset = Type.objects.get(name='jeans')

        # if not queryset.is_leaf_node():
        #     children = queryset.get_children()
        
        #     while not children[0].is_leaf_node():
        #         children = children[0].get_children()

        #     children = children[0].get_siblings(include_self=True)
        #     print(Product.objects.filter(category__in=children).values())
        # else:
        #     print(Product.objects.filter(category__in=[queryset]).values()) 

        print(get_products_by_category(category='all').values())
        print(get_products_by_category(category='bottomwear').values())
        
        assert 1==1
        
    def test_suggestions(self):
        
        print('-----------TEMP=10---------')
        suggestions_1 = compute_suggestions(temperature=10, gender='M')
        print(suggestions_1)
        
        print('-----------TEMP=16---------')
        suggestions_2 = compute_suggestions(temperature=16, gender='M')
        print(suggestions_2)

        print('-----------TEMP=24---------')
        suggestions_3 = compute_suggestions(temperature=24, gender='M')
        print(suggestions_3)
        
        
        print('-----------TEMP=30---------')
        suggestions_4 = compute_suggestions(temperature=30, gender='M')
        print(suggestions_4)
        
        print('-----------TEMP=30, FEMALE---------')
        suggestions_5 = compute_suggestions(temperature=30, gender='F')
        print(suggestions_5)
        
        assert 1==1
        
