import random
import time
from io import BytesIO
from random import randrange

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.core.cache import cache, caches
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.cache import cache_page

from App.models import Student
from App.utils import getcolor, gendratecode
from djangocache import settings


def index(request):

    return HttpResponse('hello world')


# @cache_page(30)
def news(request):
    cache = caches['redis_backend']
    result = cache.get('news')
    if result:
        return HttpResponse(result)

    new_list = []
    for i in range(10):
        new_list.append('蔡徐坤 %d' % i)
    time.sleep(5)

    context = {
        'newlist': new_list
    }
    response = render(request, 'newslist.html', context=context)
    cache.set('news', response.content, timeout=30)
    return response


@cache_page(60, cache='default')
def jokers(request):
    time.sleep(5)
    return HttpResponse('jokerlist')


def home(request):

    return HttpResponse('home')


def getphone(request):
    if randrange(100) > 90:
        return HttpResponse('恭喜获得购买资格！')
    return HttpResponse('正在排队......请勿刷新页面')


def getticket(request):
    return HttpResponse('优惠券充足！')


def search(request):
    return HttpResponse('hello world')


def calc(request):
    a = 250
    b = 250
    result = (a+b)/0
    return HttpResponse(result)


def addstudents(request):
    for i in range(100):
        student = Student()
        student.s_name = 'cxk %d' % i
        student.s_age = i
        student.save()
    return HttpResponse('创建学生成功！')


def getstudents(request):
    page = int(request.GET.get('page'))
    per_page = int(request.GET.get('perpage'))

    students = Student.objects.all()[per_page*(page-1): page*per_page]

    data = {
        'students': students
    }

    return render(request, 'students.html', context=data)


def getstudentspage(request):

    page = request.GET.get('page', 1)
    per_page = request.GET.get('perpage', 10)
    students = Student.objects.all()
    paginator = Paginator(students, per_page)
    page_object = paginator.page(page)
    data = {
        'page_object': page_object,
        'page_range': paginator.page_range,
    }
    return render(request, 'getstudentspage.html', context=data)


def getcode(request):

    mode = 'RGB'
    size = (150, 50)

    red = getcolor()
    green = getcolor()
    blue = getcolor()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)
    imagedraw = ImageDraw(image, mode=mode)
    imagefont = ImageFont.truetype(settings.FONT_PATH, size=50)
    verify_code = gendratecode()

    for i in range(4):
        fill = (getcolor(), getcolor(), getcolor())
        imagedraw.text(xy=(38*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(1000):
        fill = (getcolor(), getcolor(), getcolor())
        xy = (randrange(201), randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()
    image.save(fp, 'png')

    request.session['verifycode'] = verify_code

    return HttpResponse(fp.getvalue(), content_type='image/png')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        recvcode = request.POST.get('verifycode')
        if recvcode.lower() == request.session.get('verifycode').lower():
            request.session.flush()
            return HttpResponse('helloworld')
        return redirect(reverse('App:login'))


def maps(request):

    return render(request, 'map_test.html')


def delete_student(request):

    student = Student.objects.get(pk=1)
    student.delete()

    return HttpResponse('delete student success')