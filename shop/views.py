from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')

    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/product_list.html', {"page_obj": page_obj, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})


def category_products(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=c).order_by("-created_at")
    return render(request, 'shop/product_list.html', {"products": products})
