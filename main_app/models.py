from django.db import models

# Create your models here.

class QuoteRequest(models.Model):
    fullname = models.CharField(max_length = 200, null = True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.fullname)
    