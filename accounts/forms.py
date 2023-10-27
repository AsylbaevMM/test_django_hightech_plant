from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')


