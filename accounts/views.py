from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request=request, message="User already exists.")
                return redirect(reverse('register'))
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request=request,
                                   message="Email already exists.")
                    return redirect(reverse('register'))
                else:
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(
                        request=request, message="You are now logged in.")
                    return redirect(reverse('dashboard'))
                    # user.save()
                    # messages.success(
                    #     request=request, message="Account registered successfully.")
                    # return redirect(reverse('login'))

        else:
            messages.error(request=request, message="Password do not match.")
            return redirect(reverse('register'))
    return render(request=request, template_name="accounts/register.html", context={})


def dashboard(request):
    return render(request=request, template_name="accounts/dashboard.html", context={})


def logout(request):
    if request.method == "POST":
        auth.logout(request=request)
        messages.success(request=request, message="You are succesfully logged out.")
        return redirect(reverse('login'))
