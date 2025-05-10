from ..models import TouristSpot, Category, TourGuide, CustomUser, Booking, BookingLine, Review, Notification, PhotoGallery, Payment
from ..forms import AddReviewForm, BookingForm, BookingLineForm, PaymentForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
from django.urls import reverse
import datetime

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
    list = TouristSpot.objects.get(id=id)
    reviews = Review.objects.filter(spot=list)
    gallery = PhotoGallery.objects.filter(spotID=list)[:5]
    
    if request.method == 'POST':
        booking_list = Booking.objects.filter(user=request.user)
        bookingline_list = BookingLine.objects.filter(booking__in=booking_list)

        if 'review' in request.POST:
            reviewform = AddReviewForm(request.POST)
            if reviewform.is_valid():
                review = reviewform.save(commit=False)
                review.user = request.user
                review.spot = TouristSpot.objects.get(id=id)
                review.save()
                messages.success(request, "Review added successfully!")
                return redirect('view_touristspot', id)
            else:
                messages.error(request, "Error adding review. Please try again.")
                return redirect('view_touristspot', id)
        
        totalcost = 0
        if 'confirm_book' in request.POST:
            if 'visitDate' in request.POST and 'numberOfPeople' in request.POST:
                existing_booking = BookingLine.objects.filter(
                    booking__user=request.user,
                    visitDate=request.POST.get('visitDate')
                ).exists()

                if existing_booking:
                    messages.error(request, "You already have a booking on this date")
                    return redirect('view_touristspot', id)
                
                if int(request.POST.get('numberOfPeople')) > 10:
                    messages.error(request, "Number of people exceeds the limit")
                    return redirect('view_touristspot', id)
                
                if int(request.POST.get('numberOfPeople')) < 1:
                    messages.error(request, "Number of people must be at least 1")
                    return redirect('view_touristspot', id)
                
                if request.POST.get('visitDate') < datetime.date.today().strftime('%Y-%m-%d'):
                    messages.error(request, "Visit date cannot be in the past")
                    return redirect('view_touristspot', id)
                
                if request.POST.get('visitDate') > (datetime.date.today() + datetime.timedelta(days=365)).strftime('%Y-%m-%d'):
                    messages.error(request, "Visit date cannot be more than 1 year in the future")
                    return redirect('view_touristspot', id)

                booking = Booking()
                booking.user = request.user
                booking.save()

                bookingline = BookingLine()
                bookingline.booking = booking
                bookingline.spot = list
                bookingline.visitDate = request.POST.get('visitDate')
                bookingline.numberOfPeople = request.POST.get('numberOfPeople')
                bookingline.price = list.entrancefee
                totalcost += bookingline.price * int(bookingline.numberOfPeople);
                
                booking.totalcost = totalcost;
                bookingline.save()
                booking.save()

                messages.success(request, "Book added successfully! Next Payment. ")
                return redirect('payment', booking.id)
    else:
        booking = BookingForm()
        reviewform = AddReviewForm()
        bookingline = BookingLineForm()

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

@login_required(login_url='login')
def book_payment(request, id):
    booking = Booking.objects.get(id=id)
    bookingline = BookingLine.objects.get(booking=booking)
    spot = TouristSpot.objects.get(id=bookingline.spot.id)
    if request.method == 'POST':
        if 'pay' in request.POST:
            payment = Payment()
            payment.booking = booking
            payment.amount = booking.totalcost
            payment.paymentMethod = request.POST.get('paymentMethod')
            payment.status = 'S'
            payment.save()

            messages.success(request, "Payment successful!")
            return redirect('user_booking', request.user.id)
        
        if 'cancelpayment' in request.POST:
            bookingline.delete()
            booking.delete()
            messages.success(request, "Booking cancelled successfully!")
            return redirect('user_booking', request.user.id)
            
        if 'paylater' in request.POST:
            payment = Payment()
            payment.booking = booking
            payment.amount = booking.totalcost
            payment.paymentMethod = request.POST.get('paymentMethod')
            payment.status = 'NP'
            payment.save()

            messages.success(request, "Pay Later!")
            return redirect('user_booking', request.user.id)
    else:
        paymentform = PaymentForm()
    context = {
        'form': paymentform,
        
        'spot': spot,
        'booking': booking,
        'bookingline': bookingline,

        'title': "Payment",
        'action': "Pay",
    }
    template = loader.get_template('tourist/payment.html')
    return HttpResponse(template.render(context, request))




