from django.contrib import admin
from .models import Category, Product, Suggestion, Weather

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Suggestion)
admin.site.register(Weather)