from django import forms

from apps.salon.models.client import Client


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("active", "salon", "phone", "first_name")