from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hi Joseph,This is your firstApp up and running</h1> \n <p>Keep coding nerd,you almost there <p>')
