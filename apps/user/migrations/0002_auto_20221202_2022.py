# Generated by Django 2.2 on 2022-12-02 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': '用户信息表', 'verbose_name_plural': '用户信息表'},
        ),
    ]
