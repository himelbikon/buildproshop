from django.contrib.admin import site
from .models import *


site.register(Product)
site.register(Review)
site.register(Order)
site.register(OrderItem)
site.register(ShippingAddress)
