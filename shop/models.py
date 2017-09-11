from django.db import models

# Create your models here.

import uuid
import datetime


class TuanFeature(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return  self.name


class TuanMode(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class FoodCategory(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ShopInfo(models.Model):

    # the struct of shopInfo
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    description = models.TextField()
    vote = models.DecimalField(null=True, blank=True, default=0, max_digits=3, decimal_places=1)
    longitude = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=6)
    latitude = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=6)
    shopID = models.UUIDField(default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField(auto_now=True)

    category = models.ManyToManyField(FoodCategory)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Food(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    normal_price = models.DecimalField(max_digits=6, decimal_places=2)
    pintuan_price = models.DecimalField(max_digits=6, decimal_places=2)

    add_time = models.DateTimeField(auto_now=True)

    shop = models.ForeignKey(ShopInfo)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class FoodImages(models.Model):
    food = models.ForeignKey(Food)
    image = models.ImageField()


class PinTuan(models.Model):

    name = models.CharField(max_length=200, default='PinTuan')
    food = models.ForeignKey(Food)
    feature = models.ForeignKey(TuanFeature, null=True, blank=True, on_delete=models.SET_NULL)
    mode = models.ForeignKey(TuanMode, null=True, blank=True, on_delete=models.SET_NULL)
    food_category = models.ForeignKey(FoodCategory, null=True, blank=True, on_delete=models.SET_NULL)

    pintuan_from = models.DateTimeField()
    pintuan_end  = models.DateTimeField()

    food_from = models.DateTimeField()
    food_end  = models.DateTimeField()

    per_limit = models.IntegerField(default=1)

    if_cancel = models.BooleanField(default=False)

    total_count = models.IntegerField()
    left_count = models.IntegerField()

    create_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(null=True, blank=True)

    expires = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
