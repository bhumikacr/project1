from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Bhumika(request):
    return HttpResponse('<h1>My Name is Bhumika</h1>')
def keerthi(request):
    return HttpResponse("<h1>Bhumika's sister</h1>")
def Nalini(request):
    return HttpResponse("Bhumika's Mother")