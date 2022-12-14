# Generated by Django 2.2 on 2022-12-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254, verbose_name='用户名')),
                ('password', models.CharField(max_length=16, verbose_name='用户密码')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('headimg', models.ImageField(upload_to='', verbose_name='头像')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, verbose_name='性别')),
                ('carrer', models.CharField(max_length=20, verbose_name='职业')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('info', models.CharField(max_length=254, verbose_name='个人简介')),
            ],
        ),
    ]
