from datetime import datetime
# from django.utils import timezone

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.account.models import Account


class RegistrationForm(UserCreationForm):
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

class RegistrationByPhoneForm(forms.Form):
    first_name  = forms.CharField(label='Your name', max_length=100)
    phone       = forms.CharField(label='Phone', max_length=100)
    agree_terms = forms.BooleanField(initial=False)

    def clean(self):
        cleaned_data = super().clean()

        first_name  = cleaned_data.get('first_name')
        phone       = cleaned_data.get('phone')
        agree_terms = cleaned_data.get('agree_terms')

        try:
            account = Account.objects.get(phone=phone)
            self.add_error('phone', 'Пользователь с данным номером телефона уже зарегистрирован')
        except Account.DoesNotExist:
            pass

        if len(first_name) < 2:
            self.add_error('first_name', 'First name can\'t be less than 2 digits')

        if len(phone) < 5:
            self.add_error('phone', 'Phone can\'t be less than 5 digits')

        # if image != '' and image_url != '':
        #     self.add_error('image', 'Заполните только одно поле!')
        #     self.add_error('image_url', 'Заполните только одно поле!')

        return cleaned_data

    # def clean_phone(self):
    #     cd = self.cleaned_data
    #     if len(cd['phone']) < 5:
    #         raise forms.ValidationError("Phone can't be less than 5 digits")
    #     return cd['phone']

    # def clean_agree_terms(self):
    #     cd = self.cleaned_data
    #     return cd['agree_terms']


class EditAccountForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1950, datetime.now().year - 15)),
        # widget=forms.SelectDateWidget(),
        # initial=timezone.now()
        # initial="15 04 2014"
    )

    # birth_date = forms.CharField(
    #     # initial="2004-03-15"
    #     initial=timezone.now()
    # )

    class Meta:
        model = Account
        fields = ("phone", "email", "city", "birth_date")
