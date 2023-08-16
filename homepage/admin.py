from django.contrib import admin
from .models import CustomUser
from .models import  UserProfile
from .models import Membership
from .models import PaymentForm
from .models import GalleryImage


admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Membership)
admin.site.register(GalleryImage)
