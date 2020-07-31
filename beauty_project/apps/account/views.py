from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

# from apps.account.forms import RegistrationForm, AuthForm
from django.contrib.auth.forms import AuthenticationForm
from apps.account.forms import RegistrationForm, RegistrationByPhoneForm

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


# @login_required(login_url='/user/login/')
@login_required(login_url='user:login')
def personal_cabinet_view(request):
    context = {}
    return render(request, 'account/cabinet.html', context)


# Sandbox
def register_by_phone_view(request):
    context = {}
    if request.POST:
        # first_name  = request.POST.get('first_name')
        # phone       = request.POST.get('phone')
        # agree_terms = request.POST.get('agree_terms')

        # print(first_name)
        # print(phone)
        # print(agree_terms)

        # if first_name and phone and agree_terms == 'true':
        #     from random import randint
        #     request.session['phone'] = phone
        #     request.session['password'] = str(randint(0000, 9999))
        #     request.session.modified = True
        #     return redirect('user:registration-password')

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

    # user = User.objects.create_user(username=phone, \
    #                                 email='noemail@gmail.com', \
    #                                 first_name=first_name,
    #                                 phone=phone, \
    #                                 password=password
    #                             )

    user = User(username=phone, \
                    email='noemail@gmail.com', \
                    first_name=first_name,
                    phone=phone, \
                    password=password
                )
    user.save()

    # Set user Group
    group = Group.objects.get(name='Client')
    group.user_set.add(user)

    login(request, user)

    # del request.session['first_name']
    # del request.session['phone']
    # del request.session['password']
    # request.session.modified = True

    return render(request, 'account/register-password.html', context)