'''
This signal is for creating a profile whenever a new user was created
'''

# whenever the user is saved, send the signal
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# receive decorate, which is receive signal
from django.dispatch import receiver
from .models import Profile

# Everytime when a User instance finalize the execution of its save method, the created_profile function will be executed.
@receiver(post_save, sender=User)
# post_save signal will pass 4 arguments to below function
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()