from django.shortcuts import render
from .models import Link, Client

def index(request):
    context={}
    return render(request,'index.html',context=context)
