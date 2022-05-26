from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    url('register/',views.register),
    url('login/',views.login_view),
    url('logout/',views.logout)
]
