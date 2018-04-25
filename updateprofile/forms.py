from django import forms
from django.contrib.auth.models import User
from .models import Profile
from datetime import date, datetime
from calendar import monthrange

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Address', 'location', 'birth_date','gender','phoneno','name_on_card', 'card_number', 'expiry_date','card_code']

    def clean_phoneno(self):
            nums="0123456789"
            phoneno = self.cleaned_data.get("phoneno")
            print(phoneno)

            number = self.data['card_number']
            print(number)
            type = "Unknown"
            if len(number) == 13:
                if number[0] == "4":
                    type = "Visa"
            elif len(number) == 14:
                if number[:2] == "36":
                    type = "MasterCard"
            elif len(number) == 15:
                if number[:2] in ("34", "37"):
                    type = "American Express"
            elif len(number) == 16:
                if number[:4] == "6011":
                    type = "Discover"
                if number[:2] in ("51", "52", "53", "54", "55"):
                    type = "MasterCard"
                if number[0] == "4":
                    type = "Visa"

            value = number
            if value and (len(value) < 13 or len(value) > 16):
                raise forms.ValidationError("Please enter in a valid " + \
                                            "credit card number.")
            elif type not in ("Visa", "MasterCard",
                              "American Express"):
                raise forms.ValidationError("Please enter in a Visa, " + \
                                            "Master Card, or American Express credit card number.")
            # exp = self.data['expiry_date']
            # if date.today() > exp:
            #     raise forms.ValidationError(
            #         "The expiration date you entered is in the past.")
            if len(phoneno)!=10:
                raise forms.ValidationError("Phone number should be of 10 numbers ")

            for l in phoneno:
                if l in nums:
                    continue
                else:

                    raise forms.ValidationError("Phone number should be of numbers only")

            return phoneno

    def clean_Creditcard(self):

            return number
