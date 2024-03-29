
from django.db import models
from django.db.models import Sum
from django.conf import settings
import uuid
from products.models import Products

from accounts.models import UserProfile

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    product_id = models.IntegerField(blank=False, editable=False, default=1)
    product_name = models.CharField(max_length=32, null=False, editable=False, default="Test")
    quantity = models.IntegerField(blank=False, editable=False, default=1)
    default_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    sub_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    full_name = models.CharField(max_length=50,blank=False, default="Test")
    email = models.CharField(max_length=50, blank=False, default="Test")
    phone_number = models.CharField(max_length=50, blank=False, default="Test")
    postcode = models.CharField(max_length=50, blank=False, default="Test")
    town_or_city = models.CharField(max_length=50, blank=False, default="Test")
    street_address1 = models.CharField(max_length=50, blank=False, default="Test")
    street_address2 = models.CharField(max_length=50, blank=False, default="Test")
    county = models.CharField(max_length=50, blank=False, default="Test")

    def _generate_order_number(self):        
        return uuid.uuid4().hex.upper()

    def update_total(self):        
        self.order_total = self.lineitems.aggregate(Sum('total_cost'))['total_cost__sum']       
        
        #if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
        #    self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
       # else:
        #    self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):      
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Products, null=False, blank=False,
                                on_delete=models.CASCADE)    
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def __str__(self):
        return self.order_number

    #def save(self, *args, **kwargs):       
        #self.total_cost = self.product.price * self.quantity
        #super().save(*args, **kwargs)

    #def __str__(self):
        #return f'SKU {self.product.sku} on order {self.order.order_number}'