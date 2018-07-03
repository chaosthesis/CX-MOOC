from django import forms
from django.contrib.auth.models import User
from CXMOOC_Account.models import Passport

# User Update View
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# Passport Update View
class PassportForm(forms.ModelForm):
    
    class Meta:
        model = Passport
        exclude = ['user']