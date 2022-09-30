from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required(login_url='signup')
def index(request) :
  return render(request, 'home.html')

@login_required(login_url='signup')
def settings(request):
  return render(request, 'settings.html')

def signup(request) :
  if 'signupBottom' in request.POST:
    email = request.POST['email'];
    username = request.POST['username'];
    password = request.POST['password'];
    print(email + username + password);
    if len(password) < 6 or len(password) > 30 :
      messages.info(request, "Password should be between 6 - 30 characters.")
      return redirect('signup')
    else :
      if User.objects.filter(email=email).exists():
        messages.info(request, "Email already exists !!!")
        return redirect('signup')
        
      elif User.objects.filter(username=username).exists():
        messages.info(request, "Username already exists !!!")
        return redirect('signup')
      else:
        user = User.objects.create_user(email=email, username=username.lower(), password=password)
        user.save()

        # chuyển hướng tới page settings
        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        # tạo user mới
        user_model = User.objects.get(username=username.lower())
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('signup')

  if 'signupModal' in request.POST:
    modalEmail = request.POST['modalEmail'];
    modalUsername = request.POST['modalUsername'];
    modalPass = request.POST['modalPass'];
    print(modalEmail + modalUsername + modalPass);
    if len(modalPass) < 6 or len(modalPass) > 30 :
      messages.info(request, "Password should be between 6 - 30 characters.")
      return redirect('signup')
    else :
      if User.objects.filter(email=modalEmail).exists():
        messages.info(request, "Email already exists !!!")
        return redirect('signup')
        
      elif User.objects.filter(username=modalUsername).exists():
        messages.info(request, "Username already exists !!!")
        return redirect('signup')
      else:
        user = User.objects.create_user(email=modalEmail, username=modalUsername.lower(), password=modalPass)
        user.save()


        user_model = User.objects.get(username=modalUsername.lower())
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('signup')

  if 'btnLogin' in request.POST:
    email = request.POST['emailModal']
    password = request.POST['passModal']
    print(email + ' ' + password)
    user = auth.authenticate(username=email, password=password)
    print(user)

    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, "Login failed !!!")
      return redirect('signup')

  else :
    return render(request, 'pinterest.html')
  
@login_required(login_url='signup')
def logout(request):
  auth.logout(request)
  return redirect('signup')