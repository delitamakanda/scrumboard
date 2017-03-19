from django import forms
from .models import MiniUrl

class MiniUrlForm(forms.ModelForm):

    class Meta:
        model = MiniUrl
        fields = ('url', 'pseudo')

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args,**kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre nom:"
        self.fields['contact_email'].label = "Votre email:"
        self.fields['content'].label  = "Sujet de votre message:"
