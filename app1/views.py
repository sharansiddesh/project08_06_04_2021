from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)

    return HttpResponse(f"<h1>th addioin of {num1} and {num2} is : {num1+num2}")
    

def fact(request,num):
    num1=int(num)
    facto=1
    while num1>=2:
        facto*=num1
        num1-=1
    return HttpResponse(f"<h1>the fact of {num} is : {facto}")