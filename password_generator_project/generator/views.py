from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
    #return HttpResponse('Hello there friend')

def password(request):
    return render(request, 'generator/password.html')