from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse


def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')  
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    form=LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
        
    else:
        return render(request, 'accounts/login.html',{'form':form})
    

