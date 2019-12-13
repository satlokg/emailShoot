from django.urls import path
from user.views import profile, emaillist, emailadd, campaignlist, campaignadd
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('emailList/', emaillist, name='emaillist'),
    path('email-add/', emailadd, name='emailadd'),
    path('campaign-list/', campaignlist, name='campaignlist'),
    path('campaign-add/', campaignadd, name='campaignadd'),

]
