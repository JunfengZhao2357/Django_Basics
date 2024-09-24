from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Handle request and send response

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Junfeng'})