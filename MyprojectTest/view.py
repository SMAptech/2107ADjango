
from django.http import HttpResponse
from django.shortcuts import render

from Ecom.models import *

def anyFunction(request):
	return HttpResponse("hello")


def functionKaNaam(request):
    return HttpResponse("this is new functions")



def homeFun(request):
    student = {'name':'Ali','age':20}
    cource = {'name':'python','duration':3}
    data = {
        'student':student,
        'course' : cource
    }
    return render(request,"homt.html",data)

def layout(request):
    return render(request,"layout.html")

def add(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        description = request.POST['product_desc']
        product = Product(
            product_name = product_name,
            description = description
        )
        product.save()
        
        
    return render(request,"homt.html")


def show(request):
    product = Product.objects.all()
    data = {
        'product':product
    }

    return render(request,"footer.html",data)