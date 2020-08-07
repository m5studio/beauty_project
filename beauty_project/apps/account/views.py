from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required, user_passes_test

# from apps.account.forms import RegistrationForm, AuthForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from apps.account.forms import (
    RegistrationForm,
    RegistrationByPhoneForm,
    EditAccountForm,
    ResetPasswordForm,
)

from apps.salon.models.salon import Salon
from apps.salon.models.client import Client

from apps.salon.forms import AddClientForm

from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.models import User, Group
# TODO: change User to Account
User = get_user_model()


# TODO: remove
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
            context['form'] = form
    else: #GET request
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'account/register.html', context)


def login_view(request):
    context = {}
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user:profile')
        else:
            context['form'] = form
    else: #GET request
        form = AuthenticationForm()
        context['form'] = form
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='user:login')
def user_profile_view(request):
    context = {}

    # Clean session
    if request.session.get('first_name'):
        del request.session['first_name']
        request.session.modified = True
    if request.session.get('phone'):
        del request.session['phone']
        request.session.modified = True
    if request.session.get('password'):
        del request.session['password']
        request.session.modified = True

    if request.POST:
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
        else:
            context['form'] = form
    else: #GET request
        form = EditAccountForm(instance=request.user)
        context['form'] = form
    return render(request, 'account/profile.html', context)


@login_required(login_url='user:login')
def change_password_view(request):
    context = {}
    if request.POST:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user:profile')
        else:
            context['form'] = form
    else: #GET request
        form = PasswordChangeForm(user=request.user)
        context['form'] = form
    return render(request, 'account/profile-change-password.html', context)


# TODO
@login_required(login_url='user:login')
# @user_passes_test(lambda user: user.groups.filter(name__in=['Salon']))
@user_passes_test(lambda user: user.groups.filter(name='Salon').exists() or user.is_superuser)
def add_salon_client_view(request):
    context = {}
    if request.POST:
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
        else:
            context['form'] = form
    else: #GET request
        form = AddClientForm()
        context['form'] = form
    return render(request, 'account/profile-add-salon-client.html', context)


def register_by_phone_view(request):
    context = {}
    if request.POST:
        form = RegistrationByPhoneForm(request.POST)
        if form.is_valid():
            first_name  = form.cleaned_data['first_name']
            phone       = form.cleaned_data['phone']
            agree_terms = form.cleaned_data['agree_terms']

            # Generate password and write it to session
            from random import randint
            request.session['first_name'] = first_name
            request.session['phone'] = phone
            request.session['password'] = str(randint(0000, 9999))
            request.session.modified = True
            return redirect('user:registration-password')
        else:
            context['form'] = form
    else: #GET request
        form = RegistrationByPhoneForm()
        context['form'] = form

    return render(request, 'account/register-by-phone.html', context)


def register_password_view(request):
    context = {}

    first_name = request.session['first_name']
    phone      = request.session['phone']
    password   = request.session['password']

    user = User(username=phone, \
                    # email='noemail@gmail.com', \
                    first_name=first_name,
                    phone=phone, \
                    password=password
                )
    user.save()

    # Set user Group
    group = Group.objects.get(name='Client')
    group.user_set.add(user)

    login(request, user)
    return render(request, 'account/register-password.html', context)


def reset_password_view(request):
    context = {}
    if request.POST:
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            phone_or_email = form.cleaned_data['phone_or_email']

            # Generate new password
            # from random import randint
            # request.session['first_name'] = first_name
            # request.session['phone'] = phone
            # request.session['password'] = str(randint(0000, 9999))
            # request.session.modified = True
            # return redirect('user:registration-password')
        else:
            context['form'] = form
    else: #GET request
        form = ResetPasswordForm()
        context['form'] = form

    return render(request, 'account/reset-password.html', context)