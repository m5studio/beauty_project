from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# from apps.account.forms import RegistrationForm, AuthForm
from django.contrib.auth.forms import AuthenticationForm
from apps.account.forms import RegistrationForm

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group

User = get_user_model()


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
            return redirect('/')
        else:
            context['form'] = form
    else: #GET request
        form = AuthenticationForm()
        context['form'] = form
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')


# Sandbox
def register_by_phone_view(request):
    context = {}
    if request.POST:
        phone = request.POST.get('phone')
        print(phone)

        if phone != '':
            from random import randint
            request.session['phone'] = phone
            request.session['password'] = str(randint(0000, 9999))
            request.session.modified = True

            return redirect('user:registration-password')

            # user = User.objects.create_user(username='test', email='test@mail.ru', phone=phone, password='123')
            # user.save()

    return render(request, 'account/register-by-phone.html', context)


def register_password_view(request):
    context = {}

    phone = request.session['phone']
    password = request.session['password']

    user = User.objects.create_user(username=phone, \
                                    email='noemail@gmail.com', \
                                    phone=phone, \
                                    password=password
                                )
    user.save()

    # Set user Group
    group = Group.objects.get(name='Client')
    group.user_set.add(user)

    login(request, user)

    # del request.session['phone']
    # del request.session['password']
    # request.session.modified = True

    return render(request, 'account/register-password.html', context)