from django.contrib import admin
from .models import CustomUser, TourGuide, Category, TouristSpot, PhotoGallery, Booking, BookingLine, Review, Notification, Payment

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_tourguide')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('spotname',)

class TourGuideAdmin(admin.ModelAdmin):
    list_display = ('user', 'rate_per_day', 'years_of_experience','is_verified')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'spotID', 'caption', 'is_approved')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'totalcost', 'createdAt',)

class BookingLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'spot', 'visitDate', 'numberOfPeople', 'price',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'spot', 'rating', 'review', 'createdDate')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('userID', 'message', 'sentDate', 'isRead')
    list_filter = ('isRead',)
    search_fields = ('message',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'amount', 'paymentMethod', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('booking__user__email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TouristSpot, TouristSpotAdmin)
admin.site.register(TourGuide, TourGuideAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingLine, BookingLineAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Payment, PaymentAdmin)

admin.site.site_title = "Booking Tourist Spot Admin"
admin.site.site_header = "Booking Tourist Spot Admin"