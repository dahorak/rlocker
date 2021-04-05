from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if request.method == 'GET':
        return render(request, template_name='account/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.info(request, f"You are logged in as {user.username}")
            return redirect('dashboard_page')
        else:
            messages.error(request, 'The combination of the user name and the password is wrong!')
            return redirect('login_page')

def logout_page(request):
    logout(request)
    messages.info(request, f'You have been logged out!')
    return redirect('dashboard_page')
