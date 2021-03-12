from django import forms
from django.contrib.auth.models import User
from account.models import UserAccount


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')


class UserAccountForm(forms.ModelForm):
    # country = forms.ChoiceField(widget=forms.RadioSelect, choices=UserAccount.COUNTY_CHOICES)

    class Meta:
        model = UserAccount
        fields = ('full_address', 'city', 'postal_code', 'telephone')
