from django.db import models
from django.urls import reverse
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User

# Create your models here.
def min_length_check(val):
        if len(val) <= 10:
             raise validators.ValidationError(
                 "%(val)s Must Greater than 10", params={'val': val})

class EmailUser(models.Model):
    email_id = models.CharField(
        validators=[
            min_length_check
            ],
        max_length=255
        )
    name = models.CharField(
        max_length=255
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    objects = models.Manager
    def __str__(self):
        return self.email_id
    # def get_absolute_url(self):
    #     return reverse('emaillist',kwargs={'pk':self.pk})

class EmailUserForm(forms.ModelForm):
    class Meta:
        model = EmailUser
        fields = ['email_id', 'name', 'user']
        widgets = {
            'email_id':forms.EmailInput(attrs={'class':'form-control'}),
            'name':forms.TimeInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean(self):
        fields = self.cleaned_data
        keys = list(fields.keys())
        if(len(fields['email_id']) <= 10):
           raise validators.ValidationError("%(val)s Must Greater than 10", params={'val':keys[0]})
        
