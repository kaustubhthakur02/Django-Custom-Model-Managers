from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product

# BEFORE: In your views
def product_list(request):
    products = Product.objects.filter(available=True).order_by('-created_at')
    featured = Product.objects.filter(available=True, featured=True)

    product_data = list(products.values('id', 'name', 'price', 'stock'))
    featured_data = list(featured.values('id', 'name', 'price', 'stock'))

    return JsonResponse({
        'products': product_data,
        'featured': featured_data
    })


# AFTER: With custom manager
def product_list(request):
    products = Product.items.available().order_by('-created_at')
    featured = Product.items.featured()

    product_data = list(products.values('id', 'name', 'price', 'stock'))
    featured_data = list(featured.values('id', 'name', 'price', 'stock'))

    return JsonResponse({
        'products': product_data,
        'featured': featured_data
    })