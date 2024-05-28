from django.shortcuts import render, redirect, get_object_or_404
from review.models import Review, Border
from trips.models import TripDetail, Trip, Region
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    username = request.user.username
    trip_list = list(Trip.objects.filter(user=request.user))
    content = {
        'username':username,
        'trip_list':trip_list,
    }
    return render(request, 'expense/index.html', content)

def index2(request):
    return render(request, 'expense/index2.html')
