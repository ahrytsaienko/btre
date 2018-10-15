from django.shortcuts import render, redirect


def login(req):
    if req.method == 'POST':
        pass
    else:
        return render(req, 'accounts/login.html')


def register(req):
    if req.method == 'POST':
        pass
    else:
        return render(req, 'accounts/register.html')


def logout(req):
    return redirect('index')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
