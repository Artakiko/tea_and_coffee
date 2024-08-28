from django.urls import path
from .views import *# all functions


urlpatterns = [
   path('', catalog, name='catalog'),
   path('productdetail/<int:product_id>/',productdetail, name='product_detail'), 
   path('orders/', orders, name='orders'),
   path('make_orders/<int:product_id> /',make_orders,name='make_orders')
]