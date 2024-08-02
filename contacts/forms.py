from django import forms

from .models import CallBack


class ContactForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ["name", "phone_number", "email", "message"]
        