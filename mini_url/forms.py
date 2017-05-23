from django import forms
from .models import MiniUrl
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MiniUrlForm(forms.ModelForm):

    class Meta:
        model = MiniUrl
        fields = ('url', 'pseudo')




class SignupForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birth_date', )
