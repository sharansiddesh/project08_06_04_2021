from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def revesers(request,data):
    data1=data[::-1]
    return HttpResponse(f'<h1>the reverse of string {data} is : {data1}</h1>')
