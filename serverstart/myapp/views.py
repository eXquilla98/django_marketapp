from django.shortcuts import render


def index(request):
    return render(request, 'market/index.html')

# Create your views here.
