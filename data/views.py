from django.shortcuts import render
from data.models import Data
# Create your views here.


def index(request):
    data = Data.objects.all()
    return render(request, 'index.html', {'data': data})