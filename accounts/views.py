from django.shortcuts import render, redirect
from django.contrib import messages


def login(req):
    if req.method == 'POST':
        pass
    else:
        return render(req, 'accounts/login.html')


def register(req):
    if req.method == 'POST':
        messages.error(req, 'Testing message')
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def logout(req):
    return redirect('index')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
