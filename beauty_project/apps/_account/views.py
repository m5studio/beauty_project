from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from apps.account.forms import RegistrationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

"""
def registration_phone_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone')
            username = phone
            raw_password = '123'
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context['form'] = form
    else: #GET request
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'account/register-by-phone.html', context)
"""


def logout_view(request):
    logout(request)
    return redirect('/registration-phone/')