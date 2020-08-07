from django import forms

from apps.salon.models.client import Client


class AddClientForm(forms.ModelForm):
    # active = forms.BooleanField(initial=True, disabled=True)
    # salon  = forms.CharField(required=False)

    class Meta:
        model = Client
        # fields = ("active", "salon", "phone", "first_name")
        # fields = ("phone", "first_name")
        fields = "__all__"
        # exclude = ["active"]