from django.shortcuts import render


def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')