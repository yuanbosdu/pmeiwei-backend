from django.shortcuts import render

from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.


class ShopView(View):

    def get(self, request):

        return HttpResponse('get')

    def post(self, request):

        return HttpResponse('post')

