from ..models import TouristSpot, Category, TourGuide, CustomUser, Booking, BookingLine, Review, Notification, PhotoGallery
from ..forms import AddReviewForm, BookingForm, BookingLineForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
from django.urls import reverse

def touristspots(request):
    list = TouristSpot.objects.all()
    context = {
        'list': list,
        'title': "Tourist Spot",
        'action': "Tourist Spot",
        'category': Category.objects.all(),
        'tourguide': TourGuide.objects.all(),
    }
    template = loader.get_template('tourist/touristspots.html')
    return HttpResponse(template.render(context, request))

def touristspots(request):
    list = TouristSpot.objects.filter(is_approved=True)
    context = {
        'list': list,
        'title': "Tourist Spot",
        'action': "Tourist Spot",
        'category': Category.objects.all(),
        'tourguide': TourGuide.objects.all(),
    }
    template = loader.get_template('tourist/touristspots.html')
    return HttpResponse(template.render(context, request))

def view_touristspot(request, id):
    if request.method == 'POST':
        booking = BookingForm(request.POST)
        reviewform = AddReviewForm(request.POST)
        bookingline = BookingLineForm(request.POST)
        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.user = request.user
            review.spot = TouristSpot.objects.get(id=id)
            review.save()
            messages.success(request, "Review added successfully!")
            return redirect('view_touristspot', id)
        elif booking.is_valid() and bookingline.is_valid():
            booking = booking.save(commit=False)
            booking.user = request.user
            booking.save()
            bookingline = bookingline.save(commit=False)
            bookingline.booking = booking
            bookingline.spot = TouristSpot.objects.get(id=id)
            bookingline.save()
            messages.success(request, "Booking added successfully!")
            return redirect('view_touristspot', id)
    else:
        booking = BookingForm()
        reviewform = AddReviewForm()
        bookingline = BookingLineForm()

    list = TouristSpot.objects.get(id=id)
    reviews = Review.objects.filter(spot=list)
    gallery = PhotoGallery.objects.filter(spotID=list)[:5]
    context = {
        'list': list,
        'gallery': gallery,
        'booking': booking,
        'bookingline': bookingline,

        'reviews': reviews,
        'reviewform': reviewform,
    }
    template = loader.get_template('tourist/view_touristspots.html')
    return HttpResponse(template.render(context, request))