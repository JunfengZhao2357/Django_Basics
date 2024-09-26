from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# Create your views here.
# Handle request and send response

def say_hello(request):
    query_set = Product.objects.all()
    filtered_set = query_set.filter(unit_price__gt=20)
    filtered_set_2 = query_set.filter(unit_price__range=(20,30))
    # we can use 'pk' instead of 'id' to search for id=1 product
    # 'pk' stands for primary key and we can also use id=1 to search
    # product = Product.objects.get(pk=1)
    
    # get the total number of how many items in the table
    # total_num = Product.objects.count()
    
    # we can also filter the all query set 
    # eg, 
    # filtered_set = query_set.filter().filter().order_by()
    return render(request, 'hello.html', {'name': 'Junfeng', 'products': list(filtered_set_2)})