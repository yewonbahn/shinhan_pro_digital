from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# 로그인 페이지
# 기능 1: 로그인 화면 출력
# 기능 2: 아이디, 비밀번호 입력받아서 로그인되는것.
def signin(request):
    if request.method == 'POST':
        user_id=request.POST.get('user_id')
        password=request.POST.get('password')
        user=authenticate(request,username=user_id,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            request.POST.get('user_id'),
            request.POST.get('email'),
            request.POST.get('password'),
        )
        return redirect('/member/login/')

    return render(request, 'register.html')