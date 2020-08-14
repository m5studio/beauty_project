from django import forms

from apps.account.models import Account
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
    client   = forms.ModelChoiceField(disabled=True, queryset=Account.objects.all())
    # datetime = forms.DateTimeField(widget=forms.DateTimeInput())

    def __init__(self, *args, **kwargs):
        # Select current user in form client
        self.client = kwargs.pop('client')
        super(ClientAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['client'].initial = self.client

    class Meta:
        model = ClientAppointment
        fields = "__all__"
