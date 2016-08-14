from django.shortcuts import render
from .models import Product, Category

def home (request):

    product = Product.objects.all()
    
    context = {'product': product}
    return render (request,"index.html", context)

# Create your views here.
