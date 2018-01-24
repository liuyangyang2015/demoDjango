from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")

def song(request):
        context = {}
        context['hello'] = 'hi you are a honor !'
        return render(request, 'hello.html', context)