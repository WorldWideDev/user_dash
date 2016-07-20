from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user

class CustForm(ModelForm):
    desc = forms.CharField(label='Description', widget=forms.Textarea(attrs={'cols': 22, 'rows': 5}))
    class Meta:
        model = CustomUser
        fields = ('desc',)
    # def save(self, commit=True):
    #     cust = super(CustForm, self).save(commit=False)
    #     cust.desc = self.cleaned_data['desc']
    #     if commit:
    #         cust.save()
    #         return cust

class RegisterForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'cust': CustForm
    }
    # def dispatch_init_instance(self, name, instance):
    #     if name == 'person':
    #         return instance
    #     return super(RegisterForm, self).dispatch_init_instance(name, instance)
    # def save(self, commit=True):
    #     print 'in form save'
    #     objects = super(RegisterForm, self).save(commit=False)
    #     print objects
    #     if commit:
    #         user = objects['user']
    #         print user
    #         user.save()
    #         cust = objects['cust']
    #         cust.user = user
    #         print cust
    #         cust.save()
    #     return objects

class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    def save(self, commit=True):
        user = super(UpdateProfileForm, self).save(commit=False)
        user.username = self.cleaned_data['username']        
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user