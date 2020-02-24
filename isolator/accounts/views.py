from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegisterForm,SigninForm

# Create your views here.


"""
Django provide a lot of types Generic View and those are very flexible.
From this viewpoints,View is basically created by ClassBaseView.
"""

"""Register function"""
def join(request):
    params = {
        'form': RegisterForm(),
    }
    return render(request,'accounts/join.html',params)


"""Login Transition"""
class SigninView(LoginView):
    form_class = SigninForm
    template_name = 'accounts/signin.html'

"""Logout transition"""
class Logout(LogoutView):
    template_name = 'accounts/signin.html'

def registerUser(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('accounts:join')

    d = {'form':form,}
    return render(request,'accounts/join.html',d)