# Generated by Django 2.1.8 on 2020-05-28 11:36

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            managers=[
                ('a_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
