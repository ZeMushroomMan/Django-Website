from django.shortcuts import get_object_or_404, render
from . models import Category, Product
# Create your views here.

def home(request):
    return render(request, 'home.html' )

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def products(request):
    products = Product.objects.all()
    return render(request, 'display.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'Productdetail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

