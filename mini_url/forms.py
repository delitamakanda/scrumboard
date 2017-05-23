from django import forms
from .models import MiniUrl
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MiniUrlForm(forms.ModelForm):

    class Meta:
        model = MiniUrl
        fields = ('url', 'pseudo')
        
        
        
        
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Must be a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'email', 'password1', 'password2',)
