from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(QuoteRequest)
admin.site.register(CustomUser)
admin.site.register(Subscription)
admin.site.register(Payment_Method)
admin.site.register(Order)