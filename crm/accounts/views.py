from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password

from .models import User
from .auth_user import UserAuth as auth


def login_page(req):
    messages = []
    if req.method == 'POST':
        user = auth.authenticate(phone=req.POST['phone'], password=req.POST['passwd'])
        if user == None:
            messages.append('Неверные данные или вас нет у нас в базе, попробуйте ещё раз или обратитесь к администратору.')
        else:
            login(req, user)
            return redirect('main', 'manage')

    if req.user.is_authenticated:
        return redirect('main', 'manage')
    else:
        return render(req, 'accounts/login.html', {'messages': messages})


def logoutView(req):
    logout(req)
    return redirect('login')


def profile_page(req):
    messages = []
    if req.method == 'POST':
        data = req.POST.dict()
        psswd = data['psswd']
        user = User.objects.get(id = req.user.id)
        user.password = make_password(psswd)
        user.save()
        messages.append('Пароль изменен')

    return render(req, 'accounts/profile.html', {'user': req.user, 'messages': messages})