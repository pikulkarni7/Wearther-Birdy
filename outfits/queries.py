import typing
from .models import Product, Category, Suggestion


def get_products_by_category(category:str) -> typing.List[dict]:
    
    if category == 'all':
        return Product.objects.all()
    
    category_obj = Category.objects.get(name=category)
    
    return Product.objects.filter(category=category_obj)
    
                

def save_suggestion_history(suggestion_dict, user) -> None:
    for key in suggestion_dict:
        for Product in suggestion_dict[key]:
            Suggestion.objects.create(
                user = user,
                product = Product
            )
    

def get_saved_suggestions(date, user):
    
    return Suggestion.objects.filter(
        user = user,
        date = date
    ).order_by('product_id').distinct('product_id')
    
    