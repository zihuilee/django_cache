import hashlib
import random
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Two.models import Stu, Grade, Person, Animals, Student


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
