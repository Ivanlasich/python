from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def echo(request):
    try:
        if(request.META['REQUEST_METHOD']=='GET'):
            a = request.GET.urlencode()
            s= a.split("=")
        else:
            a = request.POST.urlencode()
            s = a.split("=")
        return render(request, 'echo.html', context={
    'check':0,'get_letter': s[0],
    'get_value': s[1],
    'request_method': request.META['REQUEST_METHOD'],
    'get_tag': request.META})
    except:

        return render(request, 'echo.html', context={
    'check':1,'get_tag': request.META})


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
