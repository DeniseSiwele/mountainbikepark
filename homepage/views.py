from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.models import User
from .models import UserProfile, Membership
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import PaymentForm
import requests
from django.conf import settings

def homepage(request):
    context = {
        'park_name': 'Roodeplaat Mountain Bike Park',  # Example data
        'location': 'Pretoria',
        'trails': ['Trail 1', 'Trail 2', 'Trail 3', 'Trail 4'],  # Example data
    }
    return render(request, 'homepage/index.html', context)

def aboutus(request):
   context = {
        'park_name1': 'Roodeplaat Mountain Bike Park',  # Example data
        'location1': 'Pretoria',  # Example data
    }
   return render(request, "homepage/aboutus.html", context)


def contactus(request):
    context = {}
    return render(request, "homepage/contactus.html")

def success(request):
    context = {}
    return render(request, "homepage/success.html")


def gallery(request):
    context = {}
    return render(request, "homepage/gallery.html")


def logout(request):
    context = {}
    return render(request, "homepage/logout.html")

def membership(request):
    context = {}
    return render(request, "homepage/membership.html")

def restaurant(request):
    context = {}
    return render(request, "homepage/restaurant.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage/index.html')
        else:
            error_message = "Invalid username or password."
            return render(request, 'homepage/login.html', {'error_message': error_message})

    return render(request, 'homepage/login.html')


def calculate_expiry_date(membership_type):
    today = datetime.now().date()
    
    if membership_type == 'annual':
        # Expiry date will be one year from today
        expiry_date = today + timedelta(days=365)
    elif membership_type == 'monthly':
        # Expiry date will be one month from today
        expiry_date = today + timedelta(days=30)
    elif membership_type == 'daily':
        # Expiry date will be one day from today
        expiry_date = today + timedelta(days=1)
    else:
        # Default to one day from today if membership type is invalid
        expiry_date = today + timedelta(days=1)
    
    return expiry_date

def register(request):
    if request.method == 'POST':
        # Retrieve user details from the form
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        age = request.POST['age']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        medical_aid_details = request.POST['medical_aid_details']
        membership_type = request.POST['membership_type']
        expiry_date = calculate_expiry_date(membership_type)  # Define this function to calculate the expiry date

        # Create user and user profile
        user = User.objects.create_user(username=username, password=password)
        user_profile = UserProfile.objects.create(
            user=user,
            name=name,
            surname=surname,
            age=age,
            gender=gender,
            date_of_birth=date_of_birth,
            medical_aid_details=medical_aid_details,
        )
        user.save()

        # Create membership
        membership = user_profile.create_membership(membership_type, expiry_date)

    return render(request, 'homepage/register.html')




def process_payment(request):
    if request.method == 'POST':
        card_number = request.POST['card_number']
        card_name = request.POST['card_name']
        expiry_date = request.POST['expiry_date']
        cvv = request.POST['cvv']

        # Construct the payment request payload
        payload = {
            'card_number': card_number,
            'card_name': card_name,
            'expiry_date': expiry_date,
            'cvv': cvv,
            # Add other required fields for Ozow payment request
        }

        # Send the payment request to Ozow
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_OZOW_API_KEY',
        }

        response = requests.post('https://api.ozow.com/api/v1/payment', json=payload, headers=headers)
        
        # Process the response from Ozow and handle success or failure
        if response.status_code == 200:
            return redirect('paymentsuccess.html')
        else:
            # Handle payment failure
            return redirect('paymentfailure.html')

    return render(request, 'membership.html')


