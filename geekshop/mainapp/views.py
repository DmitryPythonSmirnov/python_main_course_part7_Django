from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
import random


main_menu_links = [
    {'href': 'home', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    return random.sample(list(Product.objects.all()), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def home(request):
    basket = get_basket(request.user)
    title = 'магазин'
    products = Product.objects.all()[:3]
    context = {
        'title': title,
        'main_menu_links': main_menu_links,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    product_menu_links = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            categoty_item = {'name': 'все'}
        else:
            categoty_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'title': 'продукты',
            'main_menu_links': main_menu_links,
            'product_menu_links': product_menu_links,
            'products': products_list,
            'category': categoty_item,
            'basket': basket,
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/products_list.html', context)

    context = {
        'title': 'продукты',
        'main_menu_links': main_menu_links,
        'product_menu_links': product_menu_links,
        'same_products': same_products,
        'basket': basket,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    basket = get_basket(request.user)
    context = {
        'title': 'контакты',
        'main_menu_links': main_menu_links,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context)


def context(request):
    context = {
        'title': 'Test context',
        'header': 'Добро пожаловать на сайт',
        'username': 'John',
        'products': [
            {'name': 'Стулья', 'price':  6789},
            {'name': 'Диваны', 'price':  12345},
            {'name': 'Столы', 'price':  5555},
        ]
    }
    return render(request, 'mainapp/test_context.html', context)


def product(request, pk):
    product_menu_links = ProductCategory.objects.all()
    context = {
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'product_menu_links': product_menu_links,
    }
    return render(request, 'mainapp/product.html', context)
