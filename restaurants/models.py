from django.db import models

class Category (models.Model):
    category_text= models.CharField(max_length=10)
    add_date = models.DateTimeField('Date Added')


class Location (models.Model):
    location = models.CharField(max_length = 6)
    add_dt = models.DateTimeField('Date Added')

class Restaurant (models.Model):
    name_text = models.CharField(max_length = 100)
    address_text = models.CharField(max_length = 200)
    add_dte = models.DateTimeField('Date Added')

class ReviewCategory (models.Model):
    price = models.IntegerField(default = 0)
    serviceCharge = models.IntegerField(default = 0)

class ReviewRecord(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CUSCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CUSCADE)
    price = models.ForeignKey(ReviewCategory, on_delete = models.CUSCADE)
    serviceCharge = models.ForeignKey(ReviewCategory, on_delete = models.CUSCADE)

class Users (models.Model):
    