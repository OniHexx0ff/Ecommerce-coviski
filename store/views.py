from django.shortcuts import render,get_object_or_404
from .models import Category, Product




def product_all(requests):
    products = Product.products.all()
    context = {
        'products': products
    }
    return render(requests, 'store/home.html',context)

def product_detail(requests,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(requests, 'store/products/single.html',{'product':product})

def category_list(requests, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(requests, 'store/products/category.html',{'category':category,'products':products})