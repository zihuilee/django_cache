from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^getuser/', views.get_user, name='getuser'),
    url(r'^getusers/',views.get_users, name='getusers')
]