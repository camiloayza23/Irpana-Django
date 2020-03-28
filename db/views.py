from django.shortcuts import render
from db.models import Lugar
# Create your views here.

def lugar_details(request):
    obj = Lugar.objects.get(id_lugar=1)
    context = {
        'nombre': obj.nombre,
        'zona': obj.zona
    }
    return render(request,"lugar/detail.html",context)