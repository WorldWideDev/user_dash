from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.views.generic import View
from .models import User
from .forms import RegisterForm

# Create your views here.
class Register(View):
    form = RegisterForm
    template_url = 'logreg/register.html'
    def get(self, request):
        context = {'form': self.form}
        return render(request, self.template_url, context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
        else:
            context = {'form': form}
            return render(request, self.template_url, context)

class Login(View):
    form = forms.AuthenticationForm
    template_url = 'logreg/login.html'
    def get(self, request):
        context = {'form': self.form}
        return render(request, self.template_url, context)
    def post(self, request):
        form = self.form(None, request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/success')
            else:
                return render(request, self.template_url, context)
        else:
            return render(request, self.template_url, context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login')


class Success(View):
    template_url = 'logreg/success.html'
    def get(self, request):
        return render(request, self.template_url)