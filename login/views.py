from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as authorize, logout as deauth

# Create your views here.
def index(request):
    if(request.method == "POST"):
        form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Username or Password is not correct')
            return redirect('/')
        else:
            authorize(request, user)
            return redirect('/user/profile')
    else:
        if(request.user.is_authenticated):
            return redirect('/user/profile')
        form = AuthenticationForm()
    return render(request, 'index.html', {'title': 'user login', 'form': form})


def signup(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.add_message(request, messages.INFO,
                                 'User Successfully Registered')
            return redirect('/')
    return render(request, 'signup.html', {'title': 'user register', 'form': form})


def logout(request):
     if(request.user.is_authenticated):
         deauth(request)
         messages.info(request, 'You have been successfully logout')
         return redirect('/')



