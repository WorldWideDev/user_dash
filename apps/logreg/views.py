from django.shortcuts import render, redirect
from django.contrib.auth import forms, login as django_login, authenticate, logout as django_logout
#from .backends import EmailAuthBackend
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, View, UpdateView
from .models import CustomUser, Message, Comment
from .forms import CustomUserCreationForm, CustomUserChangeForm, AuthenticationForm

# Create your views here.
class Login(View):
    form = AuthenticationForm
    template_url = 'logreg/login.html'
    def get(self, request):
        context = {
            'form': self.form,
            'template_url': self.template_url
        }
        return render(request, self.template_url, context)

    def post(self, request):
        form = self.form(data=request.POST)
        context = {'form': form}
        if form.is_valid():
            print 'in valid'
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            print user

            if user is not None:
                if user.id == 1:
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                django_login(request, user)
                request.session['userId'] = user.id
                return redirect('/dashboard')
            else:
                return render(request, self.template_url, context)
        else:
            print 'not valid'
            return render(request, self.template_url, context)

class Logout(View):
    def get(self, request):
        django_logout(request)
        return redirect('login')

class Register(CreateView):
    form = CustomUserCreationForm
    form_class = CustomUserCreationForm
    template_name = 'logreg/register.html'
    def get(self, request):
        context = {
            'form': self.form,
            'template_name': self.template_name
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form(request.POST)
        #print form.errors.as_data()
        if form.is_valid():
            user = form.save()
            return redirect('/login')
        else:
            context = {
                'form': form,
                'template_name': self.template_name
            }
            print form.errors.as_data()
            return render(request, self.template_name, context)

class Edit(UpdateView):
    template_name = 'logreg/edit.html'
    form = CustomUserChangeForm
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = '/dashboard'
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'desc': user.desc
        }
        form = self.form(initial=data)
        print user
        context = {
            'user': user,
            'form': form
        }
        return render(request, self.template_name, context)

class Delete(View):
    def post(self, request):
        CustomUser.objects.filter(pk=request.POST['userId']).delete()
        return redirect('dashboard')

class Show(View):
    template_url = 'logreg/show.html'
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        messages = Message.objects.filter(recipient=user)
        comments = Comment.objects.filter(page_owner=user)
        context = {
            'user':user,
            'messages': messages,
            'comments': comments
        }
        return render(request, self.template_url, context)

class Dash(View):
    template_url = ''
    def get(self, request):
        users = CustomUser.objects.all()
        _id = request.session['userId']
        _user = CustomUser.objects.get(id = _id)
        if _user.is_staff == True:
            self.template_url = 'logreg/dashboard-admin.html'
        else:
            self.template_url = 'logreg/dashboard.html'
        context = {'users': users}
        return render(request, self.template_url, context)

class CreateMessage(View):
    def post(self, request, pk):
        Message.objects.create(
                content=request.POST['content'],
                sender = CustomUser.objects.get(pk=request.session['userId']),
                recipient = CustomUser.objects.get(pk=pk)
            )
        return redirect('dashboard')

class CreateComment(View):
    def post(self, request, pk):
        print request.POST['message_id'], 'is message id'
        Comment.objects.create(
                content=request.POST['content'],
                sender = CustomUser.objects.get(pk=request.session['userId']),
                message = Message.objects.get(pk=request.POST['message_id']),
                page_owner = CustomUser.objects.get(pk=pk)
            )
        return redirect('dashboard')
