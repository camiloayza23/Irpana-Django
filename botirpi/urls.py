from django.urls import path
from botirpi.views import home, lugar
from db.views import lugar_details

urlpatterns = [
    path('',home,name='home'),
    path(r'lugar/(?P<pk>\d+)/$', lugar, name='lugar')
]