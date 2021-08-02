from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .form import RegisterUserForm


# users can register themselves through this view
def RegisterUserView(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been successfully created. Please Login')
            return redirect('login')
    else:
        form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)


# users can login to the site via this view
def LoginUserView(request):
    """
    This view enables you to reallt customize your login page and not rely on the 
    default django login template and design.

    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Incorrect Login Details')
    return render(request, 'users/login.html')


# users can logout from this view
def LogoutUserView(request):
    logout(request)
    return redirect('login') # once they logout, it redirects them to the login page. This is customizable