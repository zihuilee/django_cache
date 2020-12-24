import hashlib
import random
import time
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Two.models import Stu, Grade, Person, Animals, Student


def verifyCode(request):
    # 引入随机函数模块
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
      20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
      xy = (random.randrange(0, width), random.randrange(0, height))
      fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
      draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
      rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    print(1)
    font = ImageFont.truetype('../../static/font/SFCompactRounded.ttf', 23)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    # del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    data = buf.getvalue()
    # # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(data)


def get_stu_grade(request):
    stu = Stu.objects.get(pk=2)
    grade = stu.s_grade
    return HttpResponse(grade.g_name)


def get_grade_stu(request):
    grade = Grade.objects.get(pk=1)

    students = grade.stu_set.all()
    context = {
        'students': students,
    }
    return render(request, 'students.html', context=context)


def add_persons(request):
    for i in range(15):
        person = Person()
        person.p_name = 'jack %d' % i
        person.p_sex = i % 2
        person.p_age = random.randrange(100)
        person.save()

    return HttpResponse('addperson success')


def get_persons(request):

    persons = Person.objects.filter(p_age__gt=50)
    context = {
        'persons': persons
    }

    return render(request, 'getpersons.html', context=context)


def add_person(request):
    person = Person.objects.create(p_name='tony')
    person.save()

    return HttpResponse('addperson success')


def get_grades(request):
    """
    :param request:
    :return:
    """
    grades = Grade.objects.all()

    return render(request, 'gradelist.html', context=locals())


def get_animals(request):

    animals = Animals.a_objects.all()
    for animal in animals:
        print(animal.a_name)
    return HttpResponse('获取成功')


def get_students(request):

    students = Student.objects.all()

    context = {
        'students': students,
        'count': 5,
    }

    return render(request, 'getstudents.html', context=context)


def get_student(request):
    return None


def students(request, g_id):
    students = Stu.objects.filter(s_grade__id=g_id)

    return render(request, 'studentlist.html', context=locals())


def add_student(request):
    if request.method == 'GET':
        return render(request, 'addstudent.html')
    elif request.method == 'POST':
        stu = Stu()
        name = request.POST.get('name')
        grade = request.POST.get('grade')
        stu.s_name = name
        stu.s_grade_id = grade
        stu.save()
        return redirect(reverse('Two:getgrades'))


def del_student(request, id):
    res = Stu.objects.filter(pk=id)
    res.delete()
    return redirect(reverse('Two:getgrades'))


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'two_login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('uname')
#         response = redirect(reverse('Two:mine'))
#         response.set_cookie('username', username,)
#         return response

def login(request):
    if request.method == 'GET':
        return render(request, 'two_login.html')
    elif request.method == 'POST':
        username = request.POST.get('uname')
        response = redirect(reverse('Two:mine'))
        request.session['username'] = username
        return response


def register(request):
    if request.method == 'GET':
        return render(request, 'two_register.html')
    elif request.method == 'POST':
        return None


def mine(request):
    # username = request.COOKIES.get('username')
    username = request.session.get('username')
    print(username)
    return render(request, 'mine.html', context=locals())


def logout(request):
    response = redirect(reverse('Two:mine'))
    # response.delete_cookie('username')
    request.session.flush()
    return response


def generate_token(ip, username):
    c_time = time.ctime()
    r = username
    return hashlib.new('md5', (ip+c_time+r).encode('utf-8')).hexdigest()


def index(request):
    return render(request, 'index.html')


def verifycodeValid(request):
    vc = request.POST['vc']
    if vc.upper() == request.session['verifycode']:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')
