from django.contrib import admin
from .models import CustomUser
from .models import  UserProfile
from .models import Membership

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Membership)