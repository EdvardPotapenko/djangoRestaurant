from django.shortcuts import render
from .models import Category, Dish, Event

# Create your views here.


def main(request):

    events = Event.objects.filter(is_visible=True)

    special_categories = Category.objects.filter(is_visible=True, is_special=True).order_by('category_order')
    for category in special_categories:
        category.dishes = Dish.objects.filter(category=category.pk)

    categories = Category.objects.filter(is_visible=True, is_special=False).order_by('category_order')
    for category in categories:
        category.dishes = Dish.objects.filter(category=category.pk)
    return render(request, 'index.html', context={'categories': categories, 'special_categories': special_categories, 'events': events})