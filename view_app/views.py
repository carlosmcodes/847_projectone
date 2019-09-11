from django.shortcuts import render

def home(request):
    return render(request, 'view_app/home.html')