from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Users

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Main')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('Main')


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = Users.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('edit')

    if request.method == "GET":
        return render(request, 'signup.html')
    
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def edit(request):
    if request.method == 'POST':
        user = request.user
        user.nickname = request.POST['nickname']
        user.user_image = request.POST.get('image')
        user.introduction = request.POST['introduction']
        user.save()

        return redirect('Main')
    return render(request, 'Profile.html')