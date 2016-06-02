from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index (request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'logreg/index.html', context)
    
def create (request):
    newUser = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = request.POST['first_name'],
    )
    print 'created a user', newUser
    return redirect('index')