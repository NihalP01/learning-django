from django.shortcuts import render
from .models import User
from django.http import HttpResponse

# Create your views here.
def firstapp(request):
    users = User.objects.all()
    return render(request, 'firstapp/index.html', {'users': users})
    