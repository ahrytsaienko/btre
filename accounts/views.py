from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(req):
    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(req, 'User already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(req, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name)
                    user.save()
                    messages.success(
                        req, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(req, "Password do not match")
            return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            messages.success(req, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(req, 'Invalid credentials')
            return redirect('login')
    else:
        return render(req, 'accounts/login.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'Your are now logged out')
        return redirect('index')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
