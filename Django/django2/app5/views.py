from django.shortcuts import render
def home(request):
    return render(request,'app5/index.html',{'param1':'Sudheera'})
# Create your views here.
