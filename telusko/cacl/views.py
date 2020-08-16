
# Create your views here.
from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Kiran'})

# whenver we are going to click the submit button then add function will be called and result.html wil be rendered
def add(request):
    # val1 = int(request.POST['num1'])
    # val2 = int(request.POST['num2'])
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1+val2
    return render(request,'result.html',{'result':res})
