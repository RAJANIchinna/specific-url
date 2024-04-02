from django.shortcuts import render
from django.http import HttpResponse

def Amma(request):
    return HttpResponse('I LOVE U AMMA')
def Nanna(request):
    return HttpResponse('<h1>Love You Nanna<h1>')
def Sister(request):
    return HttpResponse('<h1><marquee>Love You Sister</marquee></h1>')
