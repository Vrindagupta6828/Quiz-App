from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from question.models import Student
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_c = request.POST.get("password-c")
        if (password == password_c):
            user = User.objects.create_user(username, email, password);
            user.save()
            Student(student = user).save()
            messages.success(request, "Account created")
            return redirect("login")
        messages.error(request, "Password doesn't match Confirm Password")
        return render(request, "users/register.html")
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "users/register.html")

def login(request):
    if not request.user.is_authenticated:
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect('home')
        else:
            return render(request, 'users/login.html')
    else:
        return redirect("home")

def logout(request):
    auth_logout(request)
    messages.info(request, "You are now logged out")
    return redirect('home')





