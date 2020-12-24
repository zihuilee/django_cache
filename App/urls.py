from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^maps/', views.maps, name='maps'),

    url(r'^index/', views.index, name='index'),

    url(r'^news/', views.news, name='news'),

    url(r'^jokers/', views.jokers, name='jokers'),

    url(r'^home/', views.home, name='home'),

    url(r'^getphone/', views.getphone, name='getphone'),

    url(r'^getticket', views.getticket, name='getticket'),

    url(r'^search/', views.search, name='search'),

    url(r'^calc/', views.calc, name='calc'),

    url(r'^addstudents/', views.addstudents, name='addstudents'),

    url(r'deletestudent', views.delete_student, name='deletestudent'),

    url(r'^getstudents/', views.getstudents, name='getstudents'),

    url(r'^getstudentspage/', views.getstudentspage, name='getstudentspage'),

    url(r'^getcode/', views.getcode, name='getcode'),

    url(r'^login/', views.login, name='login'),
]
