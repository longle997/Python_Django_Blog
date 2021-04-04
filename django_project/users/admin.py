from django.contrib import admin
from .models import Profile

# In order to interact with model in admin site, we need to register
admin.site.register(Profile)