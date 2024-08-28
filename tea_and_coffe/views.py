from django.shortcuts import render
from .models import Product,Order
# Create your views here
def catalog (request):
    products = Product.objects.all()
    return render(request, 'tea_and_coffe/catalog.html', {'products':products}) 

def productdetail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'tea_and_coffe/productdetail.html', {'product':product} )
    
def orders (request):
    orders = Order.objects.all()
    return render(request, 'tea_and_coffe/orders.html', {'orders':orders})

def make_orders(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        Order.objects.create(
            product=product,
            address=request.POST.get('address')
            
        )
    return render(request,'tea_and_coffe/make_orders.html',{'product':product} )
 