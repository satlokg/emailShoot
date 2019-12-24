from django.urls import reverse_lazy
from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate
from user.models import EmailUser, EmailUserForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class profile(TemplateView):
    template_name = 'profile.html'


class emaillist(TemplateView):
    template_name = 'emaillist.html'
    model = EmailUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

class emailadd(FormView):
    template_name = 'emailadd.html'
    form_class = EmailUserForm
    success_url = '/'


class emailsave(CreateView):
    model = EmailUser
    fields = '__all__'
    success_url = reverse_lazy('emaillist')

class emailedit(UpdateView):
    model = EmailUser
    fields = '__all__'


class emaildelete(DeleteView):
    model = EmailUser
    success_url = reverse_lazy('emaillist')
    


class campaignlist(TemplateView):
    template_name = 'campaignlist.html'
    


class campaignadd(FormView):
    template_name = 'campaignadd.html'
    form_class = EmailUserForm
    success_url = '/'
