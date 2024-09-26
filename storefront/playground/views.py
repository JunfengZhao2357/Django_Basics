from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from store.models import Product


# Create your views here.
# Handle request and send response

def say_hello(request):
    # Products: inventory < 10 AND price < 20
    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # Products: inventory < 10 OR price < 20, we need to use Q object to realize 'OR'
    query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # Q and: Q(inventory__lt=10) & Q(unit_price__lt=20)
    # not Q: ~Q(inventory__lt=10)
    
    # filtered_set = query_set.filter(unit_price__gt=20)
    # filtered_set_2 = query_set.filter(unit_price__range=(20,30))
    
    # we can use 'pk' instead of 'id' to search for id=1 product
    # 'pk' stands for primary key and we can also use id=1 to search
    # product = Product.objects.get(pk=1)
    
    # get the total number of how many items in the table
    # total_num = Product.objects.count()
    
    # we can also filter the all query set 
    # eg, 
    # filtered_set = query_set.filter().filter().order_by()
    return render(request, 'hello.html', {'name': 'Junfeng', 'products': list(query_set)})