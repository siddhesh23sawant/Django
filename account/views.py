from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username = username).exists():
                print('User Name Taken...')
                messages.info(request, 'User Name Taken...')
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                print('Email Id already Registered')
                messages.info(request, 'Email Id already Registered')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name)
                user.save();
                print('okay its working...')
                return redirect('/')

        else:
            print("password doesn't matches")
            messages.info(request, "password doesn't matches")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')


    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')