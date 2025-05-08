from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Phone Number'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id' : 'password',
        'placeholder': '**********'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id' : 'confirm-password',
        'placeholder': '**********'
    }))
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'address', 'password1', 'password2')
        
class CustomAunthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id' : 'password',
        'placeholder': '**********'
    }))
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class AddUserAdminForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Phone Number'
    }), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id' : 'password',
        'placeholder': '**********'
    }))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
    'accept': 'image/jpeg,  image/png, image/webp',
    }), required=False)
    is_staff = forms.BooleanField(required=False)
    is_tourguide = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'username', 'phone', 'address', 'password1', 'image', 'is_staff', 'is_tourguide'

class EditUserAdminForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Phone Number'
    }), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address'
    }), required=False)
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'accept': 'image/jpeg,  image/png, image/webp',
    }), required=False)
    is_staff = forms.BooleanField(required=False)
    is_tourguide = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'phone', 'address', 'username', 'image', 'is_staff', 'is_tourguide'

class AddCategoryAdminForm(forms.ModelForm): 
    class Meta:
        model = Category
        fields = 'name', 'parent'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category Name'})
        }

class EditCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = 'name', 'parent'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category Name'})
        }

days =(
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
)

class AddTouristSpotAdminForm(forms.ModelForm):
    is_approved = forms.BooleanField(required=False)

    class Meta:
        model = TouristSpot
        fields = 'spotname', 'address', 'description', 'entrancefee', 'openingday', 'openinghours', 'category', 'is_approved', 'image', 'createdby'
        widgets = {
            'spotname': forms.TextInput(attrs={'placeholder': 'Enter Spot Name', 'required': True}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Location Address ', 'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description ', 'required': False}),
            'entrancefee': forms.NumberInput(attrs={'placeholder': 'Enter entrance fee', 'required': True}),
            'openinghours': forms.TimeInput(attrs={'type': 'time', 'required': True}),
            'image': forms.ClearableFileInput(attrs={'required': False, 'accept': 'image/jpeg,  image/png, image/webp',}),
        }

class EditTouristSpotAdminForm(forms.ModelForm):
    is_approved = forms.BooleanField(required=False)

    class Meta:
        model = TouristSpot
        fields = 'spotname', 'address', 'description', 'entrancefee', 'openingday', 'openinghours', 'category', 'is_approved', 'image', 'createdby'
        widgets = {
            'spotname': forms.TextInput(attrs={'placeholder': 'Enter Spot Name', 'required': True}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Location Address ', 'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description ', 'required': False}),
            'entrancefee': forms.NumberInput(attrs={'placeholder': 'Enter entrance fee', 'required': True}),
            'openinghours': forms.TimeInput(attrs={'type': 'time', 'required': True}),
            'image': forms.ClearableFileInput(attrs={'required': False, 'accept': 'image/jpeg,  image/png, image/webp',}),
        }

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'review': forms.Textarea(attrs={'placeholder': 'Enter your review', 'required': True}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'totalcost']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'totalcost': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }

class BookingLineForm(forms.ModelForm):
    class Meta:
        model = BookingLine
        fields = ['spot', 'visitDate', 'numberOfPeople', 'price']
        widgets = {
            'spot': forms.Select(attrs={'required': True}),
            'visitDate': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'numberOfPeople': forms.NumberInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }