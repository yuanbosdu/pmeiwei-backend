from django.contrib import admin
from .models import ShopInfo, TuanFeature, TuanMode, PinTuan, FoodCategory, Food, FoodImages

# Register your models here.

admin.site.register([ShopInfo, TuanMode, TuanFeature, PinTuan, FoodImages, FoodCategory, Food])



