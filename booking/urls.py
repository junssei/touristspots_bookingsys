from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import views, adminViews, touristViews

urlpatterns = [
    # Main Page
    path('', views.main, name='main'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('aboutus/contact', views.aboutus, name='contact'),

    path('accounts/login', views.user_login, name='login'),
    path('accounts/logout', views.user_logout, name='logout'),
    path('accounts/register', views.register, name='register'),
    path('accounts/<int:id>/profile', views.user_profile, name='profile'),
    path('accounts/<int:id>/delete', views.delete_profile, name='delete_profile'),
    path('accounts/<int:id>/profile/edit', views.edit_profile, name='edit_profile'),
    path('accounts/<int:id>/changepassword', views.change_password, name='change_password'),
    
    # User Booking
    path('accounts/<int:id>/booking', views.user_booking, name='user_booking'),
    path('accounts/<int:id>/booking/view', views.view_booking, name='view_booking'),
    path('accounts/<int:id>/booking/edit', views.edit_booking, name='edit_booking'),
    path('accounts/<int:id>/booking/cancel', views.delete_booking, name='delete_booking'),

    # Admin Page
    path('ts-admin', adminViews.admin_dashboard, name='admin_dashboard'),
    
    # Admin - Users and Roles
    path('ts-admin/users/', adminViews.users, name='users'),
    path('ts-admin/users/add', adminViews.add_user, name='add_user'),
    path('ts-admin/users/<int:id>/view', adminViews.view_user, name='view_user'),
    path('ts-admin/users/<int:id>/edit', adminViews.edit_user, name='edit_user'),
    path('ts-admin/users/<int:id>/delete', adminViews.delete_user, name='delete_user'),

    # Admin - Tourist Spot
    path('ts-admin/touristspot/', adminViews.spot, name='spot'),
    path('ts-admin/touristspot/add', adminViews.add_spot, name='add_spot'),
    path('ts-admin/touristspot/<int:id>/view', adminViews.view_spot, name='view_spot'),
    path('ts-admin/touristspot/<int:id>/edit', adminViews.edit_spot, name='edit_spot'),
    path('ts-admin/touristspot/<int:id>/delete', adminViews.delete_spot, name='delete_spot'),
    path('ts-admin/touristspot/pending', adminViews.pending_spot, name='pending_spot'),

    # Admin - Category
    path('ts-admin/touristspot/category/', adminViews.category, name='category'),
    path('ts-admin/touristspot/category/add', adminViews.add_category, name='add_category'),
    path('ts-admin/touristspot/category/<int:id>/view', adminViews.view_category, name='view_category'),
    path('ts-admin/touristspot/category/<int:id>/edit', adminViews.edit_category, name='edit_category'),
    path('ts-admin/touristspot/category/<int:id>/delete', adminViews.delete_category, name='delete_category'),

    # Admin - Booking
    path('ts-admin/booking/', adminViews.booking, name='booking'),
    path('ts-admin/booking/add', adminViews.booking_add, name='add_booking'),
    path('ts-admin/booking/<int:id>/view', adminViews.booking_view, name='view_booking'),
    path('ts-admin/booking/<int:id>/edit', adminViews.booking_edit, name='edit_booking'),
    path('ts-admin/booking/<int:id>/delete', adminViews.booking_delete, name='delete_booking'),

    # Admin - Gallery
    path('ts-admin/gallery/', adminViews.gallery, name='gallery'),
    path('ts-admin/gallery/add', adminViews.add_gallery, name='add_gallery'),
    path('ts-admin/gallery/<int:id>/view', adminViews.view_gallery, name='view_gallery'),
    path('ts-admin/gallery/<int:id>/edit', adminViews.edit_gallery, name='edit_gallery'),
    path('ts-admin/gallery/<int:id>/delete', adminViews.delete_gallery, name='delete_gallery'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customer
urlpatterns += [
    path('touristspots/', touristViews.touristspots, name='touristspots'),
    path('touristspots/<int:id>/view', touristViews.view_touristspot, name='view_touristspot'),
    path('touristspots/<int:id>/payment', touristViews.book_payment, name='payment')
]

