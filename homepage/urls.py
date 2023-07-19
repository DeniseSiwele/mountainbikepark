from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.homepage, name ="index"),
    path('aboutus/', views.aboutus, name ="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('gallery/', views.gallery, name ="gallery"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('membership/', views.membership, name ="membership"),
    path('register/', views.register, name ="register"),
    path('restaurant/', views.restaurant, name ="restaurant"),
    path('success/', views.success, name ="success"),
    path('payment/', views.process_payment, name='process_payment')
]
