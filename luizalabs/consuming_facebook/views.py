from django.shortcuts import render
from luizalabs.consuming_facebook.forms import PersonForm

# Create your views here.


def home(request):
    form = PersonForm()
    return render(request, 'home.html', {'form': form})
