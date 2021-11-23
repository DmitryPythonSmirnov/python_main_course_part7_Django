from django.shortcuts import render


# Create your views here.

main_menu_links = [
    {'href': 'home', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def home(request):
    context = {
        'title': 'магазин',
        'main_menu_links': main_menu_links
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'продукты',
        'main_menu_links': main_menu_links
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


def menu_products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    return render(request, 'inc_categories_menu.html', links_menu)