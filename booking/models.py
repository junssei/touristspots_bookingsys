
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 1MB
    if image.size > max_size:
        raise ValidationError("Image size should not exceed 1MB.")

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30, unique=True, blank=True)
    image = models.ImageField(
        upload_to='profiles', blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp']),
            validate_image_size
        ])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_tourguide = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class TourGuide(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rate_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(blank=True)
    language = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    specialties = models.CharField(max_length=200)
    licence_number = models.CharField(max_length=50)
    operating_areas = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Tour Guide: {self.user.email}"
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

days =(
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
)

status =(
    ('PENDING', 'Pending'),
    ('REJECTED', 'Rejected'),
    ('APPROVED', 'Approved'),
)

class TouristSpot(models.Model):
    image = models.ImageField(upload_to='spots', blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp']),
            validate_image_size
        ])
    spotname = models.CharField(max_length=50, unique=True, blank=False)
    address = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    entrancefee = models.IntegerField()
    openingday = models.CharField(max_length=15, choices=days, default="MON")
    openinghours = models.TimeField(default='00:00:00')
    createdDate = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdby = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.spotname
    
class PhotoGallery(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    spotID = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    caption = models.TextField(default="Lorem ipsum dolor, sit amet consectetur adipisicing elit.")
    uploadDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery', blank=True, null=True, 
    validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp']),
        validate_image_size
    ])

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - " + str(self.spotID) + " - " + str(self.userID)
    
class Booking(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    totalcost = models.DecimalField(max_digits=10, decimal_places=2,  default=1)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

class BookingLine(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=1)
    spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, default=1)
    visitDate = models.DateField(default='2025-10-10')
    numberOfPeople = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    def __str__(self):
        return str(self.booking)
    
class Notification(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    sentDate = models.DateTimeField(default=timezone.now)
    isRead = models.BooleanField(default=False) 

rating =(
    ('1', 'Bad'),
    ('2', 'Poor'),
    ('3', 'Average'),
    ('4', 'Good'),
    ('5', 'Excellent')
)

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    rating = models.CharField(choices=rating, default="1", max_length=10)
    review = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review) + str(self.user) + " - " + str(self.spot) + " - " + str(self.rating)
