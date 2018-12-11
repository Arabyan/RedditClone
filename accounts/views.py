from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate( username=request.POST['username'], password=request.POST['username'])
        if user is not None:
            login(request, user)
            return render(request, 'accounts/signup.html', {'error': 'Login successful!'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'The Username adn password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')