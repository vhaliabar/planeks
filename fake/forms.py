#from django import Widget
from django import forms
from .models import Test
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'job', 'email', 'age', 'company')
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            
        }
        


