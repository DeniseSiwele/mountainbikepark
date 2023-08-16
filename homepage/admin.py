<<<<<<< HEAD
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
=======
from django.contrib import admin
from .models import CustomUser
from .models import  UserProfile
from .models import Membership

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Membership)
>>>>>>> 912af2183e0e4d9cd7a893729a28c015950a4761
