from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home
def index(request):
    context = {}
    return render(request, 'index.html', context)

