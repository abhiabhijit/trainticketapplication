from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, help_text='Optional.')

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ( 'username','name', 'email', 'password1', 'password2' )
    # def clean_email(self):
    #     email=self.cleaned_data.get("email")
    #     qs=User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("email is taken")
    #     return email
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
class PasswordForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

class changepass(forms.Form):

    password=forms.CharField(widget=forms.PasswordInput(),min_length=6)
