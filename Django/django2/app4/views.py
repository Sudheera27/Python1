from django.shortcuts import render
def home(request):
    num1=6
    result1=square(num1)
    result2=factorial(num1)
    return render(request,'app4/index.html',{'param1':result1,'param2':result2,'param3':num1})
# Create your views here.
def square(n1):
    return n1*n1
def factorial(n1):
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1
