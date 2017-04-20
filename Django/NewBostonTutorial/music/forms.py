from django.contrib.auth.models import User
from django import forms

#this is blueprint for how we want the user registration to be taken care of

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password']