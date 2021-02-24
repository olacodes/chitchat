from django.shortcuts import render
from .models import Thread
# Create your views here.

def index(request):
  threads = Thread.objects.all()
  return render(request, 'index.html', {'threads': threads})
  