from django.shortcuts import render

def loginView(request):
    return render(request, 'login.html')

def homeView(request):
    return render(request, 'home.html')
