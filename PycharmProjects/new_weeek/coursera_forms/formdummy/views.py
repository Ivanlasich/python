import json

from django import forms
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator

from .models import Item, Review


class GoodForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(max_length=1024)
    price = forms.IntegerField(min_value=1, max_value=1000000)


class ReviewForm(forms.Form):
    text = forms.CharField(max_length=1024)
    grade = forms.IntegerField(min_value=1, max_value=10)


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):

    def post(self, request):
        form = GoodForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Item.objects.create(**cd)
            return JsonResponse(cd, status=201)
        return JsonResponse(status=400, data={})


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):


    def post(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
        form = ReviewForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cd['item'] = item
            Review.objects.create(**cd)
        return JsonResponse(status=400, data={})

class GetItemView(View):

    def get(self, request, item_id):
        try:
            b = Item.objects.get(id=item_id)
            dict = model_to_dict(b)
            d = Review.objects.filter(item=b).order_by('-id')[0:5]
            list = []
            for c in d:
                p = model_to_dict(c)
                p.pop('item')
                list.append(p)
            dict["reviews"] = list

            return JsonResponse(dict, status=200)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
