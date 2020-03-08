
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'Accounts/register.html', {'user_error': 'username taken!!!'})
            if User.objects.filter(email=email).exists():
                return render(request, 'Accounts/register.html', {'email_error': 'email id already registered!!!'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')
        else:
            return render(request, 'Accounts/register.html', {'password_error': 'password not matching!!!'})
    else:
        return render(request, 'Accounts/register.html')

    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../')
        else:
            # print('user not found')
            return render(request, 'Accounts/login.html', {'error': "Invalid credentials !!!"})
    else:
        return render(request, 'Accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile(request, user_id):
    return render(request, 'Accounts/UserProfile.html')