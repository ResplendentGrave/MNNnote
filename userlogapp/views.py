from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['passwordagain']

        if password != password_again:
            messages.error(request, '再入力パスワードが違います！')
            return render(request, 'signup.html', {'errormassage':'再入力パスワードが違います！'})
        print(password_again)
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'そのusernameは既に存在しています。')
            return render(request, 'signup.html', {'errormassage':'そのusernameは既に存在しています。'})
    return render(request, 'signup.html', {})



def loginfunc(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            mnnvoice_url = reverse('mnnvoice_app:mnnvoice_home')
            return redirect(mnnvoice_url)
        else:
            messages.error(request, 'ログインに失敗しました。')
            return render(request, 'login.html', {'errormassage':'ログインに失敗しました。再度ログインしてください。'})
    return render(request, 'login.html', {})