from django.http import HttpResponse
from django.shortcuts import render #renderizar o template html criado

def hello(request):
    return render(request, 'index.html')



 