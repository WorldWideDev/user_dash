from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.views.generic import View
from .models import User
from .forms import RegisterForm, UpdateProfileForm

# Create your views here.
class Register(View):
    form = RegisterForm
    template_url = 'logreg/register.html'
    def get(self, request):
        context = {
            'form': self.form,
            'template_url': self.template_url
        }
        return render(request, self.template_url, context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        else:
            context = {'form': form}
            return render(request, self.template_url, context)

class Login(View):
    form = forms.AuthenticationForm
    template_url = 'logreg/login.html'
    def get(self, request):
        context = {
            'form': self.form,
            'template_url': self.template_url
        }
        return render(request, self.template_url, context)
    def post(self, request):
        form = self.form(None, request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print user
            
            if user is not None:
                if user.id == 1:
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                login(request, user)
                request.session['userId'] = user.id
                return redirect('/dashboard')
            else:
                return render(request, self.template_url, context)
        else:
            return render(request, self.template_url, context)

class Logout(View):
    def get(self, request):
        logout(request)
        del request.session['user']
        return redirect('/login')


class Success(View):
    template_url = 'logreg/success.html'
    def get(self, request):
        return render(request, self.template_url)

class Dash(View):
    users = User.objects.all()
    template_url = ''
    def get(self, request):
        _id = request.session['userId']
        _user = User.objects.get(id = _id)
        if _user.is_staff == True:
            self.template_url = 'logreg/dashboard-admin.html'
        else:
            self.template_url = 'logreg/dashboard.html'
        context = {'users': self.users}
        return render(request, self.template_url, context)

class Edit(View):
    template_url = 'logreg/edit.html'
    form = UpdateProfileForm
    def get(self, request, id):
        user = User.objects.get(id = id)
        context = {
            'user': user,
            'form': self.form
        }
        return render(request, self.template_url, context)
    def post(self, request, id):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        else:
            context = {'form': form}
            return render(request, self.template_url, context)
