# -*- coding: UTF-8 -*-

from django.conf.urls import url
from .views import ShopView

urlpatterns = [
    url(r'^$', ShopView.as_view(), name='shopview')
]
