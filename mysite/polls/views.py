from django.shortcuts import render
import sqlite3

# Create your views here.
from django.http import HttpResponse


def index(request,x,y):
    z = int(x) + int(y)
    return HttpResponse("Hello, world. %s" %(str(z)))

def Hello(request):
    return HttpResponse("Hello, res2.")

