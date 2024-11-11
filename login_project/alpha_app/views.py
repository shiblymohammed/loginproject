from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache


@never_cache
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 

    error = ''
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=uname, password=pass1)
        
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password'

    return render(request, 'login.html', {'error': error})

@never_cache
@login_required 
def dashboardPage(request):
    return render(request, 'dashboard.html')



@never_cache
def logoutPage(request):
    if request.user.is_authenticated:
        if request.POST:
            logout(request)
            return redirect('login')
        return redirect('dashboard')
    return redirect('login')



def new(request):
    return render(request, 'new.html')