from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.


def profile(request):
    if(request.user.is_authenticated):
        return render(request, 'profile.html')
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')


def emaillist(request):
    if(request.user.is_authenticated):
        return render(request, 'emaillist.html')
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')


def emailadd(request):
    if(request.user.is_authenticated):
        return render(request, 'emailadd.html')
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')


def campaignlist(request):
    if(request.user.is_authenticated):
        return render(request, 'campaignlist.html')
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')


def campaignadd(request):
    if(request.user.is_authenticated):
        return render(request, 'campaignadd.html')
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')
