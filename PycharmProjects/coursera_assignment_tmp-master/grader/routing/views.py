from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
# Create your views here.
def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

def slug_route(request):
    s = request.path
    return HttpResponse(s.split('/')[3])

def sum_route(request):

    s = request.path
    c = s.split('/')
    a = int(c[3])
    b = int(c[4])
    return HttpResponse(a + b)


def sum_get_method(request):
    if request.method == 'GET':
        try:
            a = int(request.GET['a'])
            b = int(request.GET['b'])
        except:
            return HttpResponse(status=400)
        return HttpResponse(a+b)
    else:
        return HttpResponse(status=405)

def sum_post_method(request):
    if request.method == 'POST':
        try:
            a = int(request.POST['a'])
            b = int(request.POST['b'])
        except:
            return HttpResponse(status=400)
        return HttpResponse(a+b)
    else:
        return HttpResponse(status=405)
