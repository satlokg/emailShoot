from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from user.models import EmailUser, EmailUserForm

# Create your views here.


def profile(request):
    if(request.user.is_authenticated):
        return render(request, 'profile.html')
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')


def emaillist(request):
    if(request.user.is_authenticated):
        data = EmailUser.objects.all()
        return render(request, 'emaillist.html', {'title': 'Add New Email Id', 'rows': data})
    else:
        messages.info(request, 'You need to login first')
        return redirect('/')


def emailadd(request):
    if(request.user.is_authenticated):
        form = EmailUserForm()
        if request.method == 'POST':
            form = EmailUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/user/emailList/')
        return render(request, 'emailadd.html', {'title': 'Add New Email Id', 'form': form})
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
