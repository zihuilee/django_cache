from django.db import models

# Create your models here.


class Grade(models.Model):
    g_name = models.CharField(max_length=20)


class Stu(models.Model):
    s_name = models.CharField(max_length=20)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class Person(models.Model):
    p_name = models.CharField(max_length=20, db_column='name')
    p_age = models.IntegerField(default=18, db_column='age')
    p_sex = models.BooleanField(default=True, db_column='sex')

    class Meta:
        db_table = 'people'


class AnimalManager(models.Manager):
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=True)


class Animals(models.Model):
    a_name = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

    a_objects = AnimalManager()


class Student(models.Model):
    s_name = models.CharField(max_length=20)