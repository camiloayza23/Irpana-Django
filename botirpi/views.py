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
    if request.method == "POST":
        lugares = Lugar.objects.all()
        tipo_id = int(request.POST['select-tipo'])
        zona_id = int(request.POST['select-zona'])
        pcont = {
            'lugares': lugares,
            'tipo_id': tipo_id,
            'zona_id': zona_id
        }
        return render(request,"detail.html",pcont)
    return render(request,'home.html',context)

def lugar(request, pk=None):
    if pk:
        lugar = Lugar.objects.get(id_lugar=int(pk))
        lcont ={
            'lugar':lugar,
        }
        return render(request,"lugar.html",lcont)
    return HttpResponse("Hello this is the index")

