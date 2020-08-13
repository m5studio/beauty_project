from django import forms

from apps.salon.models.client import Client
from apps.salon.models.client_appointment import ClientAppointment
from apps.salon.models.salon import Salon


class AddClientForm(forms.ModelForm):
    # active = forms.BooleanField(initial=True, disabled=True)
    # salon  = forms.CharField(required=False)

    class Meta:
        model = Client
        # fields = ("phone", "first_name")
        fields = "__all__"
        # exclude = ["active"]


class EditSalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = "__all__"
        exclude = ["active"]


class ClientAppointmentForm(forms.ModelForm):
    class Meta:
        model = ClientAppointment
        fields = "__all__"
