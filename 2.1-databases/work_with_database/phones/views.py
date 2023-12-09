from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    items = Phone.objects.all()
    sort_dc = {'name': 'name',
               'min_price': 'price',
               'max_price': '-price'}
    
    if request.GET.get('sort'):
        sort = request.GET['sort']
        items = items.order_by(sort_dc[sort]) 

    
    context = {'phones': items}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    items = Phone.objects.get(slug=slug)
    
    context = {'phone': items}
    return render(request, template, context)

'''sort=name">названию</a>
   sort=min_price">начиная с дешёвых</a>
    sort=max_price">'''
