from django.urls import path
from login.views import index, signup, logout
urlpatterns = [
    path('', index),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

]
