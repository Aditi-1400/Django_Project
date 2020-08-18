from django.db.models.signals import post_save
#signal that is fired after an objects that is saved
from django.contrib.auth.models import User # sender
from django.dispatch import receiver

# this is the receiver which reveives this sdignal 
# and performs some task bascially gonna create a function

from .models import Profile

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user = instance)




# when a user is saved, send a signal which is received by the function
#and when the user is created, create it's profile

# creating s save profile funciton

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

