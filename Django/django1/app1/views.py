from django.shortcuts import render
def home(request):
    n1=5
    result=square(n1)
    return render(request,'app1/index.html',{'param1':result,'param2':n1})
def square(n1):
    return n1*n1