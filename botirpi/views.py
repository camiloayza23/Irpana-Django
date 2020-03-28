from django.shortcuts import render
from django.http import HttpResponse
from db.models import Lugar, Tipos, Zonas
# Create your views here.

def home_view(*args,**kwargs):
    return HttpResponse("Hello this is the index")
def home(request):
    tipos = Tipos.objects.all()
    zonas = Zonas.objects.all()
    context = {
        'zonas': zonas,
        'tipos': tipos
    }
    return render(request,'home.html',context)