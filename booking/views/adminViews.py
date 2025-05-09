from ..models import CustomUser, TouristSpot, Category, TourGuide
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
from django.urls import reverse
from datetime import datetime

@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('main')   
    template = loader.get_template('admin/dashboard.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

# Admin Views - Users
@login_required(login_url='login')
def users(request):
    list = CustomUser.objects.all()
    template = loader.get_template('admin/users/main.html')
    context = {
        'title': "user",
        'list': list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully!")
            return HttpResponseRedirect(reverse('users'))
        else:
            messages.error(request, "Invalid")
            return HttpResponseRedirect(reverse('add_user'))
    else:
        form = AddUserAdminForm()
    context = {
        'action': "Add",
        'title': "User",
        'form': form
    }
    template = loader.get_template('admin/users/add.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def view_user(request, id):
    list = CustomUser.objects.get(id=id)
    template = loader.get_template('admin/users/view.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))

def edit_user(request, id):
    list = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        form = EditUserAdminForm(request.POST, request.FILES, instance=list)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successfully!")
            return redirect('view_user', id)
        else:
            messages.error(request, "Update failed!")
            return redirect('edit_user', id)
    else:
        form = EditUserAdminForm(instance=list)
    context = {
        'action': "Edit",
        'title': "User",
        'form': form,
        'list': list,
    }
    template = loader.get_template('admin/users/edit.html')
    return HttpResponse(template.render(context, request))

def delete_user(request, id):
    list = CustomUser.objects.get(id=id)
    if request.method == "POST":
        list.delete()
        messages.success(request, "Deleted successfully!")
        return HttpResponseRedirect(reverse('users'))
    
    context = {
        'list': list,
    }
    template = loader.get_template('admin/users/delete.html')
    return HttpResponse(template.render(context, request))

# Admin Views - TouristSpot
@login_required(login_url='login')
def spot(request):
    list = TouristSpot.objects.all()
    template = loader.get_template('admin/spot/main.html')
    context = {
        'list': list,
        'action': '',
        'title': "Tourist Spot",
        'subtitle': 'tourist_spot',
    }
    return HttpResponse(template.render(context, request))

def add_spot(request):
    if request.method == 'POST':
        form = AddTouristSpotAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully!")
            return HttpResponseRedirect(reverse('spot'))
        else:
            messages.error(request, "Invalid")
            return HttpResponseRedirect(reverse('add_spot'))
    else:
        form = AddTouristSpotAdminForm()
    context = {
        'form': form,
        'action': "Add",
        'title': "Tourist Spot",
    }
    template = loader.get_template('admin/spot/add.html')
    return HttpResponse(template.render(context, request))

def view_spot(request, id):
    list = TouristSpot.objects.get(id=id)
    template = loader.get_template('admin/spot/view.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))

def edit_spot(request, id):
    list = TouristSpot.objects.get(id=id)
    if request.method == 'POST':
        form = EditTouristSpotAdminForm(request.POST,  request.FILES, instance=list)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successfully!")
            return redirect('view_spot', id)
        else:
            messages.error(request, "Update failed!")
            return redirect('edit_spot', id)
    else:
        form = EditTouristSpotAdminForm(instance=list)
    context = {
        'form': form,
        'list': list,
        'action': "Edit",
        'title': "Tourist Spot",
    }
    template = loader.get_template('admin/spot/edit.html')
    return HttpResponse(template.render(context, request))

def delete_spot(request, id):
    list = TouristSpot.objects.get(id=id)
    if request.method == "POST":
        list.delete()
        messages.success(request, "Deleted successfully!")
        return HttpResponseRedirect(reverse('spot'))
    
    context = {
        'list': list,
        'action': "Delete",
        'title': "Tourist Spot",
    }
    template = loader.get_template('admin/spot/delete.html')
    return HttpResponse(template.render(context, request))

def pending_spot(request):
    list = TouristSpot.objects.filter(is_approved=False)
    template = loader.get_template('admin/spot/pending.html')
    context = {
        'list': list,
        'action': 'Pending',
        'title': "Tourist Spot",
        'subtitle': 'tourist_spot',
    }
    return HttpResponse(template.render(context, request))

# Admin Views - Category
@login_required(login_url='login')
def category(request):
    list = Category.objects.all()
    template = loader.get_template('admin/category/main.html')
    context = {
        'list': list,
        'action': '',
        'title': "Categories",
        'subtitle': 'category',
        'fields': ['name', 'parent']
    }
    return HttpResponse(template.render(context, request))

def add_category(request):
    if request.method == 'POST':
        form = AddCategoryAdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully!")
            return HttpResponseRedirect(reverse('category'))
        else:
            messages.error(request, "Invalid")
            return HttpResponseRedirect(reverse('add_category'))
    else:
        form = AddCategoryAdminForm()
    context = {
        'form': form,
        'action': "Add",
        'title': "Category",
    }
    template = loader.get_template('admin/category/add.html')
    return HttpResponse(template.render(context, request))

def view_category(request, id):
    list = Category.objects.get(id=id)
    template = loader.get_template('admin/category/view.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))

def edit_category(request, id):
    list = Category.objects.get(id=id)
    if request.method == 'POST':
        form = EditCategoryAdminForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successfully!")
            return redirect('view_category', id)
        else:
            messages.error(request, "Update failed!")
            return redirect('edit_category', id)
    else:
        form = EditCategoryAdminForm(instance=list)
    context = {
        'form': form,
        'list': list,
        'action': "Edit",
        'title': "Category",
    }
    template = loader.get_template('admin/category/edit.html')
    return HttpResponse(template.render(context, request))

def delete_category(request, id):
    list = Category.objects.get(id=id)
    if request.method == "POST":
        list.delete()
        messages.success(request, "Deleted successfully!")
        return HttpResponseRedirect(reverse('category'))
    
    context = {
        'list': list,
        'action': "Delete",
        'title': "Category",
    }
    template = loader.get_template('admin/category/delete.html')
    return HttpResponse(template.render(context, request))

# Admin Views - Booking
@login_required(login_url='login')
def booking(request):
    template = loader.get_template('admin/booking/main.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def booking_add(request):
    template = loader.get_template('admin/booking/add.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def booking_view(request, id):
    template = loader.get_template('admin/booking/view.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def booking_edit(request, id):
    template = loader.get_template('admin/booking/edit.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def booking_delete(request, id):
    template = loader.get_template('admin/booking/delete.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

# Admin Views - Gallery
@login_required(login_url='login')
def gallery(request):
    list = TouristSpot.objects.all()
    template = loader.get_template('admin/gallery/main.html')
    context = {
        'list': list,
        'action': '',
        'title': "Gallery",
        'subtitle': 'gallery',
    }
    return HttpResponse(template.render(context, request))

def add_gallery(request):
    if request.method == 'POST':
        form = AddTouristSpotAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully!")
            return HttpResponseRedirect(reverse('gallery'))
        else:
            messages.error(request, "Invalid")
            return HttpResponseRedirect(reverse('add_gallery'))
    else:
        form = AddTouristSpotAdminForm()
    context = {
        'form': form,
        'action': "Add",
        'title': "Tourist Spot",
    }
    template = loader.get_template('admin/gallery/add.html')
    return HttpResponse(template.render(context, request))

def view_gallery(request, id):
    list = TouristSpot.objects.get(id=id)
    template = loader.get_template('admin/gallery/view.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))

def edit_gallery(request, id):
    list = TouristSpot.objects.get(id=id)
    if request.method == 'POST':
        form = EditTouristSpotAdminForm(request.POST,  request.FILES, instance=list)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successfully!")
            return redirect('gallery', id)
        else:
            messages.error(request, "Update failed!")
            return redirect('gallery', id)
    else:
        form = EditTouristSpotAdminForm(instance=list)
    context = {
        'form': form,
        'list': list,
        'action': "Edit",
        'title': "Tourist Spot",
    }
    template = loader.get_template('admin/gallery/edit.html')
    return HttpResponse(template.render(context, request))

def delete_gallery(request, id):
    list = TouristSpot.objects.get(id=id)
    if request.method == "POST":
        list.delete()
        messages.success(request, "Deleted successfully!")
        return HttpResponseRedirect(reverse('gallery'))
    
    context = {
        'list': list,
        'action': "Delete",
        'title': "Tourist Spot",
    }
    template = loader.get_template('admin/gallery/delete.html')
    return HttpResponse(template.render(context, request))