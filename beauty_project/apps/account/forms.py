from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.account.models import Account


class RegistrationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     # do not require password confirmation
    #     del self.fields['username']
    #     del self.fields['password1']
    #     del self.fields['password2']

    username = forms.CharField(max_length=100, help_text='Required. Add a valid username')
    email    = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    phone    = forms.CharField(max_length=100, help_text='Required. Add a valid phone number')

    class Meta:
        model = Account
        fields = ("username", "email", "phone", "password1", "password2")

    # def clean_username(self):
    #     cd = self.cleaned_data
    #     if cd['username'] == '':
    #         cd['username'] = cd['phone']
    #         # raise forms.ValidationError('Username is empty ((')
    #     return cd['username']

    # def clean_phone(self):
    #     cd = self.cleaned_data
    #     if cd['phone'] == '':
    #         raise forms.ValidationError('Phone is empty ((')
    #     return cd['phone']

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password2'] == '':
    #         cd['password2'] = '123'
    #     # if cd['password'] != cd['password2']:
    #     #     raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']


# class AuthForm(AuthenticationForm):
#     username = forms.CharField(max_length=100, help_text='Required. Add a valid username')
#     email    = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
#     phone    = forms.CharField(max_length=100, help_text='Required. Add a valid phone number')

#     class Meta:
#         fields = ("username", "email", "phone", "password")