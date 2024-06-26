import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Products
from accounts.models import UserProfile


class Orders(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=60, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_id = models.CharField(max_length=254, null=False, blank=False,
                                 default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Orders, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Products, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)


class Reviews(models.Model):
    order = models.ForeignKey(Orders, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='reviews')
    review_title = models.CharField(max_length=240, null=False,
                                    blank=False, default='')
    review_body = models.TextField(null=False, blank=False, default='')
    stars = models.SmallIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
