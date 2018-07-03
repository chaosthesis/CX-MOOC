from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from CXMOOC_Account.forms import UserForm, PassportForm

# User Register View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "account/signup.html", {'form': form})


# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your account is disabled.")
        else:
                return HttpResponse("Wrong username/password.")
    else:
        return render(request, "account/login.html")


# User Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def update_view(request):
    usrform = UserForm(request.POST, instance=request.user)
    ppform = PassportForm(request.POST, instance=request.user.passport)
    if request.method == 'POST':
        if usrform.is_valid and ppform.is_valid():
            usrform.save()
            ppform.save()
            return HttpResponseRedirect("/")
    else:
        usrform = UserForm(instance=request.user)
        ppform = PassportForm(instance=request.user.passport)
    
    return render(request, 'account/account_update.html', {'usrform': usrform, 'ppform': ppform})
