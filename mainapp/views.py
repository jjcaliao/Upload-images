from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Item
import os
  
# Create your views here.
def index(request):
    products = Item.objects.all()
    context = {'products':products}
    return render(request, 'main.html', context)

def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'addimage.html')

def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'edit.html', context)

def deleteProduct(request, pk):
    prod = Item.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request,"Product Deleted Successfuly")
    return redirect('/')