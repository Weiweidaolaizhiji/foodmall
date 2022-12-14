# Generated by Django 2.2 on 2022-12-02 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20221202_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='carrer',
            field=models.CharField(default='', max_length=20, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='city',
            field=models.CharField(default='', max_length=20, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='info',
            field=models.CharField(default='', max_length=254, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='nickname',
            field=models.CharField(default='', max_length=20, verbose_name='昵称'),
        ),
    ]
