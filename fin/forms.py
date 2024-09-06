from django import forms

from fin.models import Transfer, Profile, BankAccount
from django.contrib.auth.forms import UserCreationForm
from core.models import User


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avater']


class TransferForm(forms.ModelForm):

    class Meta:
        model = Transfer
        fields = "__all__"


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']


class BankAccountForm(forms.ModelForm):

    class Meta:
        model = BankAccount
        fields = "__all__"
        exclude = ['user']
