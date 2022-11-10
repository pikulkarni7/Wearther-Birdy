import typing
from django.core import serializers

from .models import Product, Category
from .serializers import ProductSerializer


def compute_suggestions(temperature:float, gender:str) -> dict:

    result = {}

    __bottom__ = Product.objects.none()
    __top_must__ = Product.objects.none()
    __top_optional_1__ = Product.objects.none()
    __top_optional_2__ = Product.objects.none()
    
    __diff_temp__ = 26.00 - temperature
    
    #check for female user
    if temperature >= 24 and gender == 'F':
        result['women'] = Product.objects.filter(category=Category.objects.get(name='women')).values()
        return result
    
    #bottom
    bottom = Category.objects.get(name='bottomwear')
       
    if temperature < 24:
       __bottom__ = __bottom__.union(
                Product.objects.filter(
                    category = bottom,
                    weather_value__gt = 2
                )
            ) 
    else:
        __bottom__ = __bottom__.union(
            Product.objects.filter(
                category = bottom,
                weather_value__lte = 2         #shorts
            )
        )
        
    #upperwear
    
    top_required = Category.objects.get(name='top_required')
    top_optional_1 = Category.objects.get(name='top_optional_1')
    top_optional_2 = Category.objects.get(name='top_optional_2')

    if __diff_temp__ <= 0:
        __top_must__ = __top_must__.union(
            Product.objects.filter(
                category = top_required,
                weather_value__lt = 5
            )
        )
        
    elif __diff_temp__ > 0:
        __top_must__ = __top_must__.union(
            Product.objects.filter(
                category = top_required,
                weather_value__lt = 5
            )
        )
        
        __top_optional_1__ = __top_optional_1__.union(
            Product.objects.filter(
                category = top_optional_1,                
            )
        )
        
        if  __diff_temp__ > 6:
            __top_optional_1__ =  __top_optional_1__.union(
                Product.objects.filter(
                     category = top_optional_1,
                     weather_value__lt = 10,
                     weather_value__gte = 5 
                )
            )            
        
        if __diff_temp__ > 15:
            __top_optional_2__ = __top_optional_2__.union(
                Product.objects.filter(
                    category = top_optional_2
                )
            )
    
    result['bottom'] =  __bottom__
    result['top_must'] =  __top_must__
    result['top_optional_1'] = __top_optional_1__
    result['top_optional_2'] =  __top_optional_2__
    
    return result
