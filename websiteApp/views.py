from django.shortcuts import render
from .models import Category, Dish

# Create your views here.


def main(request):
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for category in categories:
        category.dishes = Dish.objects.filter(category=category.pk)
    return render(request, 'index.html', context={'categories': categories})