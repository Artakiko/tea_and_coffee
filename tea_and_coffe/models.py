from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=40)
    price = models.FloatField(default=10.0)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/products/photo')
    discounts = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default = 0)
    is_available = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title    

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    address =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

