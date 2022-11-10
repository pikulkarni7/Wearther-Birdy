import typing
from .models import Product, Category


def get_products_by_category(category:str) -> typing.List[dict]:
    
    if category == 'all':
        return Product.objects.all()

    # if queryset.is_leaf_node():
        
    #     children = queryset.get_children()
    #     while not children[0].is_leaf_node():
    #         children = children[0].get_children()
    #     children = children[0].get_siblings(include_self=True)
        
    #     return Product.objects.filter(category__in=children)
            
    # else:
    #     return Product.objects.filter(category==queryset)
    category_obj = Category.objects.get(name=category)
    
    return Product.objects.filter(category=category_obj)
    
                

    