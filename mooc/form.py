from django import forms
from .models import Contact,Confession

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Name','Email','Insta','Comments']

class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ['Confess']