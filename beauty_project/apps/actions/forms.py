from django import forms

from apps.actions.models import Actions


class AddActionsForm(forms.ModelForm):
    # active = forms.BooleanField(initial=True, disabled=True)
    # salon  = forms.CharField(required=False)

    class Meta:
        model = Actions
        # fields = ("phone", "first_name")
        fields = "__all__"
        # exclude = ["active"]