from django.shortcuts import render
def home(request):
    result=mults(3,8)
    return render(request,'app1/index.html',{'param1':result})
def mult(n1):
    list1=[]
    for i in range(1,11,1):
        list1.append(str(n1)+"*"+str(i)+"="+str(n1*i))
    return list1
def mults(start,end):
    masterlist=[]
    for i in range(start,end+1,1):
        masterlist.append(mult(i))
    return masterlist
