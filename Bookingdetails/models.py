from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from phonenumber_field.modelfields import PhoneNumberField

class Ticketdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainname = models.CharField(max_length=30, blank=False)
    source = models.CharField(max_length=30, blank=False)
    destination = models.CharField(max_length=30, blank=False)
    pnr         = models.CharField(max_length=10, unique=True)
    journey_date = models.DateField( blank=False)
    # phoneno = PhoneNumberField()
    no_of_passengers=models.CharField(max_length=10, )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
         return self.user.username


# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()