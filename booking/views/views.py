from ..forms import CustomUserCreationForm, CustomAunthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
from django.urls import reverse

from ..models import CustomUser, Booking, BookingLine, TouristSpot, Payment
from django.utils import timezone

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

@login_required(login_url='login')
def user_profile(request, id):
    list = CustomUser.objects.get(id=id)
    template = loader.get_template('accounts/profile.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def edit_profile(request, id):
    template = loader.get_template('accounts/edit_profile.html')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return HttpResponse(template.render({ 'form': form }, request))

def change_password(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user.set_password(password)
            user.save()
            messages.success(request, "Password changed successfully!")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
    context = {
    }
    template = loader.get_template('accounts/change_password.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def delete_profile(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Profile deleted successfully!")
        return redirect('main')
    context = {
        'user': user,
    }
    template = loader.get_template('accounts/delete_profile.html')
    return HttpResponse(template.render(context, request))

# User Bookings
def user_booking(request, id):
    booking = Booking.objects.filter(user=id)
    if not booking.exists():
        context = {
            'title': "My Bookings",
            'action': "My Bookings",
        }
    else:
        payment = Payment.objects.get(booking__in=booking)
        bookingline = BookingLine.objects.get(booking__in=booking)
        context = {
        'booking': booking,
        'payment': payment,
        'bookingline': bookingline,

        'title': "My Bookings",
        'action': "My Bookings",
    }
        
    template = loader.get_template('accounts/bookings/booking.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def view_booking(request, id):
    booking = Booking.objects.get(id=id)
    context = {
        'booking': booking,
        'title': "Booking Details",
        'action': "Booking Details",
    }
    template = loader.get_template('accounts/bookings/view.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def edit_booking(request, id):
    booking = Booking.objects.get(id=id)
    if request.method == 'POST':
        booking.status = request.POST.get('status')
        booking.save()
        messages.success(request, "Booking updated successfully!")
        return redirect('user_booking')
    context = {
        'booking': booking,
        'title': "Edit Booking",
        'action': "Edit Booking",
    }
    template = loader.get_template('accounts/edit_booking.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def delete_booking(request, id):
    booking = Booking.objects.get(id=id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted successfully!")
        return redirect('user_booking')
    context = {
        'booking': booking,
        'title': "Delete Booking",
        'action': "Delete Booking",
    }
    template = loader.get_template('accounts/delete_booking.html')
    return HttpResponse(template.render(context, request))



