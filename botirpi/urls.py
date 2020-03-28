from django.urls import path
from botirpi.views import home
from db.views import lugar_details

urlpatterns = [
    path('',home,name='home'),
    path('product/',lugar_details),
]