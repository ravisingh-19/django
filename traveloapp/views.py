from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'destination/1.png'

    dest2 = Destination()
    dest2.name = 'Gurgaon'
    dest2.img = 'destination/2.png'

    dest3 = Destination()
    dest3.name = 'Noida'
    dest3.img = 'destination/3.png'

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
