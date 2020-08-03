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

class RegistrationByPhoneForm(forms.Form):
    first_name  = forms.CharField(label='Your name', max_length=100)
    phone       = forms.CharField(label='Phone', max_length=100)
    agree_terms = forms.BooleanField(initial=False)

    def clean(self):
        cleaned_data = super().clean()

        first_name  = cleaned_data.get('first_name')
        phone       = cleaned_data.get('phone')
        agree_terms = cleaned_data.get('agree_terms')

        # if first_name is None:
        #     self.add_error('first_name', 'Укажите имя!')

        # if phone is None:
        #     self.add_error('first_name', 'Укажите имя!')

        try:
            account = Account.objects.get(phone=phone)
            self.add_error('phone', 'Пользователь с данным номером телефона уже зарегистрирован')
        except Account.DoesNotExist:
            listing = None

        # if image != '' and image_url != '':
        #     self.add_error('image', 'Заполните только одно поле!')
        #     self.add_error('image_url', 'Заполните только одно поле!')

        return cleaned_data

    def clean_first_name(self):
        cd = self.cleaned_data
        if len(cd['first_name']) < 2:
            raise forms.ValidationError("First name can't be less than 2 characters")
        return cd['first_name']

    # def clean_phone(self):
    #     cd = self.cleaned_data
    #     if len(cd['phone']) < 5:
    #         raise forms.ValidationError("Phone can't be less than 5 digits")
    #     return cd['phone']

    def clean_agree_terms(self):
        cd = self.cleaned_data
        return cd['agree_terms']