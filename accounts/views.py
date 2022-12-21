from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Usuario registrado con exito!')
            return redirect('register')


    context = {
        'form': form,
    }
    return render(request,'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'el usuario o clave es incorrecto')
            return redirect('login')

    return render(request,'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "vuelve pronto!")
    return redirect('login')
 
