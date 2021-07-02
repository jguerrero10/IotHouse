from django.shortcuts import render
from django.utils import timezone

def home(request):
    time_now = timezone.now()
    context = {'time': time_now}
    return render(request, 'home.html', context)
