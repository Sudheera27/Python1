from django.shortcuts import render
def home(request):
    result=listfiles("C:/sample")
    return render(request,'app3/index.html',{'param1':result})
def listfiles(dir1):
    import os
    os.chdir(dir1)
    list1=list(os.listdir())
    list2=[]
    for i in list1:
        if os.path.isfile(i):
            list2.append(i)
    return list2
