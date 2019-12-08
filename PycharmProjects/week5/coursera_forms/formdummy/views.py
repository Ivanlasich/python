from django.shortcuts import render
from django.views import View
import requests

class FormDummyView(View):
    def get(self, request):
        r = requests.get('https://api.github.com/events')
        return render(request,'form.html',{})
