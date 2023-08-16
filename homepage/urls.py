<<<<<<< HEAD
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
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
>>>>>>> 912af2183e0e4d9cd7a893729a28c015950a4761
