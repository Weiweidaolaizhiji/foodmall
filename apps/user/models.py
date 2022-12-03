from datetime import datetime

from django.db import models

# Create your models here.

class UserModel(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    username = models.EmailField(verbose_name='用户名')
    password = models.CharField(max_length=16,verbose_name='用户密码')
    nickname = models.CharField(max_length=20,verbose_name='昵称',default='')
    headimg = models.ImageField(verbose_name='头像')
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,verbose_name='性别',default='Male')
    carrer = models.CharField(max_length=20,verbose_name='职业',default='')
    city = models.CharField(max_length=20,verbose_name='城市',default='')
    info  = models.CharField(max_length=254,verbose_name='个人简介',default='')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


