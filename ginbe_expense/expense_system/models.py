from django.db import models

# Create your models here.

class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=254)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    who_pay = models.CharField(max_length=254)
    public_private = models.CharField(max_length=30)
    inputer = models.CharField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)

class GeneralSetting(models.Model):
    man_rent_fee = models.DecimalField(max_digits=8, decimal_places=2)
    women_rent_fee = models.DecimalField(max_digits=8, decimal_places=2)