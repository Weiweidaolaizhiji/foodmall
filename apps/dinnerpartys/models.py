from django.db import models
from apps.user.models import BaseModel

class DinnerPartysModel(BaseModel):
    PALY_WAYS = [
        ('1','先到先得'),
        ('2','双向选择'),
        ('3','大数据匹配'),
    ]
    DEFALET_TAGS = [
        ('1','单身派对'),
        ('2','英式下午茶'),
        ('3','二次元'),]
    title = models.CharField(max_length=254,verbose_name='活动标题')
    price = models.CharField(max_length=5,verbose_name='活动价格')
    numbers = models.IntegerField(verbose_name='报名人数')
    startime = models.DateTimeField(auto_now=False,verbose_name='活动开始时间')
    endtims = models.DateTimeField(auto_now=False,verbose_name='活动截止时间')
    playways = models.CharField(max_length=1,choices=PALY_WAYS,verbose_name='活动玩法')
    tags = models.CharField(max_length=3,choices=DEFALET_TAGS,verbose_name='默认标签')
    inputag = models.CharField(max_length=60,verbose_name='输入标签')
    pictures =models.ImageField(verbose_name='活动照片')

    class Meta:
        verbose_name = '饭局活动表'
        verbose_name_plural = verbose_name