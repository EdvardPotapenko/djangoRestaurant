from django.contrib import admin
from .models import Category, Dish, Event
# Register your models here.


admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Event)