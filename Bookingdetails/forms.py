from django import forms
from django.contrib.auth.models import User
from .models import Ticketdetails
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ticketdetails
        fields = ['user', 'trainname', 'source','destination','pnr','journey_date','no_of_passengers','gender']