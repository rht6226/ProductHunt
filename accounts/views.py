from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        #USER wants to sign up
        if request.POST['password1'] == request.POST['password2']:
            #Entered passwords are identical
            try:
                #check if user already exists in database if yes raise error
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                #username is available
                user = User.objects.create_user(username =request.POST['username'], password= request.POST['password1'])
                auth.login(request, user)
                return redirect('main')

    else:
        #other stuff
        return render(request, 'signup.html')