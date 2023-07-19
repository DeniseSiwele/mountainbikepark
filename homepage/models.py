from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django import forms
class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    medical_aid = models.CharField(max_length=100)
    medical_aid_number = models.CharField(max_length=100)
    ice_contact = models.CharField(max_length=100)
    ice_name = models.CharField(max_length=100)

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    medical_aid_details = models.TextField()

    def create_membership(self, membership_type, expiry_date):
        membership = Membership.objects.create(user_profile=self, type=membership_type, expiry_date=expiry_date)
        return membership

class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('annual', 'Annual'),
        ('monthly', 'Monthly'),
        ('daily', 'Daily'),
    ]

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES)
    start_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def is_active(self):
        return self.expiry_date >= timezone.now().date()

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount')
    email = forms.EmailField(label='Email')