from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


main_menu_links = [
    {'href': 'home', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

product_menu_links = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

def home(request):
    title = 'магазин'
    products = Product.objects.all()[:3]
    context = {
        'title': title,
        'main_menu_links': main_menu_links,
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

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
        }
        return render(request, 'mainapp/products_list.html', context)

    same_products = Product.objects.all()[3:5]

    context = {
        'title': 'продукты',
        'main_menu_links': main_menu_links,
        'product_menu_links': product_menu_links,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'контакты',
        'main_menu_links': main_menu_links
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

