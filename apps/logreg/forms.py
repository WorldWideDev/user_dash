from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Textarea

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        print self.fields
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "desc"]
        widgets = {
            'desc': Textarea(attrs={
                'cols': 22,
                'rows': 5,
                'placeholder': 'Tell us about yourself!'
            }),
        }

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)

        #this is so exclude works for removing password
        [self.fields.pop(f) for f in self.fields.keys() if f in self.Meta.exclude]

        print self.fields, 'is fields'

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "desc"]
        widgets = {
            'desc': Textarea(attrs={
                'cols': 22,
                'rows': 5,
                'placeholder': 'Tell us about yourself!'
            }),
        }
        exclude = ("password",)

# class AuthenticationForm(forms.Form):
#     """
#     Login form
#     """
#     email = forms.EmailField(widget=forms.widgets.TextInput)
#     password = forms.CharField(widget=forms.widgets.PasswordInput)
#
#     class Meta:
#         fields = ['email', 'password']

# class RegistrationForm(forms.ModelForm):
#     email = forms.EmailField(widget=forms.TextInput, label='Email', required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
#     password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")
#
#
#     def clean(self):
#         print 'in clean method'
#         """
#         Verifies that the values entered into the password fields match
#
#         NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
#         """
#         cleaned_data = super(RegistrationForm, self).clean()
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError("Passwords don't match. Please enter again")
#         return self.cleaned_data
#
#     def save(self, commit=True):
#         print 'in save method'
#         user = super(RegistrationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#             print user, 'is user'
#         return user
#
#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2']
#
class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        print 'in clean'
        cleaned_data = super(AuthenticationForm, self).clean()
        print cleaned_data, 'is cleaned data'
        return self.cleaned_data

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
