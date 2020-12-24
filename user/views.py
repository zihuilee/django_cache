from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def get_user(request):
    username = 'jack'
    password = 'admin1237'
    users = User.objects.filter(u_name=username)
    # if users.count():
    if users.exists():
        user = users.first()
        if user.u_password == password:
            return HttpResponse('获取用户信息成功')
        else:
            return HttpResponse('密码错误')
    else:
        return HttpResponse('用户不存在')


def get_users(request):
    users = User.objects.all()[1:3]
    context = {
        'users': users
    }
    return render(request, 'get_users.html', context=context)
