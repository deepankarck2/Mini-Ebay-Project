from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

#View related to login and show message
class viewLogin(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_url = 'store-home'
    success_message = "Successfully logged in"

# View related to register
def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please Login')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form' : form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')