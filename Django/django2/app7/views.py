from django.shortcuts import render
from app7.forms import inputform1
def home(request):
    if request.method=="POST":
        form1=inputform1(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            num1=data.get("input1")
            result1 = square(num1)
            result2 = factorial(num1)
            return render(request,'app7/index.html',{'param1':result1,'param2':result2,'param3':num1,'form':form1})
    else:
        form1=inputform1()
    return render(request,"app7/index.html",{'form':form1})
        
def square(n1):
    return n1*n1
def factorial(n1):
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1