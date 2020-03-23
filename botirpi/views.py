from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(*args,**kwargs):
    return HttpResponse("Hello this is the index")
def home(request):
    return render(request,'home.html',{})