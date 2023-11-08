from django.shortcuts import render, redirect
from MbogaApp.models import Username


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = Username(firstname=request.POST['firstname'],
                            lastname=request.POST['lastname'],
                            username=request.POST['username'],
                            email=request.POST['email'],
                            password=request.POST['password'])
        username.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Username.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            username = Username.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'username': username})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
