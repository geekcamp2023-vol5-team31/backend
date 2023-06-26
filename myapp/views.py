from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Logged in.")
        else:
            return HttpResponse("Invalid credentials.")
    else:
        return render(request, 'login.html')