from django.urls import path
from user.views import profile, emaillist, emailadd, emailedit, emaildelete, emailsave, campaignlist, campaignadd
urlpatterns = [
    path('profile/', profile.as_view(), name='profile'),
    path('emailList/', emaillist.as_view(), name='emaillist'),
    path('<int:id>/emailedit/', emailedit.as_view(), name='emailedit'),
    path('<int:id>/emaildelete/', emaildelete.as_view(), name='emaildelete'),
    path('emailsave/', emailsave.as_view(), name='emailsave'),
    path('email-add/', emailadd.as_view(), name='emailadd'),
    path('campaign-list/', campaignlist.as_view(), name='campaignlist'),
    path('campaign-add/', campaignadd.as_view(), name='campaignadd'),

]
