from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^getstugrade/', views.get_stu_grade, name='getstugrade'),

    url(r'^getgradestu/', views.get_grade_stu, name='getgradestu'),

    url(r'^addpersons/', views.add_persons, name='addpersons'),

    url(r'^getpersons/', views.get_persons, name='getpersons'),

    url(r'^addperson/', views.add_person, name='addperson'),

    url(r'^getgrades/', views.get_grades, name='getgrades'),

    url(r'^students/(\d+)/', views.students, name='students'),

    url(r'^getanimals/', views.get_animals, name='getanimals'),

    url(r'^getstudents/', views.get_students, name='getstudents'),

    url(r'^addstudent/', views.add_student, name='addstudent'),

    url(r'^delstudent/(?P<id>\d+)', views.del_student, name='delstudent'),

    url(r'^login/', views.login, name='login'),

    url(r'^register/', views.register, name='register'),

    url(r'^mine/', views.mine, name='mine'),

    url(r'^logout/', views.logout, name='logout'),

    url(r'^verifycode/', views.verifyCode, name='verifycode'),

    url(r'^index/', views.index, name='index'),

    url(r'^verifycodeValid/', views.verifycodeValid, name='verifycodeValid'),
]