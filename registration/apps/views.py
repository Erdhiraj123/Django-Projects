from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistration
from django.contrib import messages
# Create your views here.
def show(request):
    if request.method=='POST':
        fm=UserRegistration(request.POST)
        if fm.is_valid():
            messages.success(request,'Thank you for submiting')
            fm.save()
    else:
        fm=UserRegistration()
    return render(request,'home.html',{'form':fm})
