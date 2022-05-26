from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    url('covid',views.covid),
    url('malaria',views.malaria),
    url('pneumonia',views.pneumonia)
]