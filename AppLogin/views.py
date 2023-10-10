from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def registerUser(req):
    form = RegisterForm()
    if(req.method == 'POST'):
        form = RegisterForm(req.POST)
        if (form.is_valid()):
            form.save()
            messages.success(req, "Account Successfully Created!")
            return HttpResponseRedirect(reverse('AppLogin:login'))
    return render(req, 'AppLogin/register.html', context={'form':form})
def loginUser(req):
    form = AuthenticationForm()
    if(req.method == 'POST'):
        form = AuthenticationForm(data=req.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(req, user)
                messages.success(req, f"Successfully Logged in! Welcome, @{username}")
                return HttpResponseRedirect(reverse('AppStream:index'))
            else:
                messages.error(req, 'Check your Credentials Again!')
        else:
            messages.warning(req, 'Please Fix the errors.')
    return render(req, 'AppLogin/login.html', context={'form':form})
@login_required
def logoutUser(req):
    logout(req)
    return HttpResponseRedirect(reverse('AppLogin:login'))