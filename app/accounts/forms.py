from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser


class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Username'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'example@mail.com'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': '*********'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': '*********'}))

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Firstname'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Lastname'}))

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name']


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'example@mail.com'}))


