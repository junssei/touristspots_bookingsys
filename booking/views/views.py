from ..forms import CustomUserCreationForm, CustomAunthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
from django.urls import reverse

# Create your views here.
def main(request):
    template = loader.get_template('main.html') 
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('accounts/register.html')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return HttpResponse(template.render({ 'form': form }, request))

def user_login(request):
    template = loader.get_template('accounts/login.html')
    if request.method == 'POST':
        form = CustomAunthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    messages.success(request, 'Login Successfully.')
                    return redirect('admin_dashboard')
                else:
                    login(request, user)
                    messages.success(request, 'Login Successfully.')
                    return redirect('main')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAunthenticationForm()
    return HttpResponse(template.render({ 'form': form }, request))

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('main')

def aboutus(request):
    context = {
    }
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render(context, request))
