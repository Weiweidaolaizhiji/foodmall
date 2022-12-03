from django.db import models
from apps.user.models import BaseModel,UserModel
from apps.dinnerpartys.models import DinnerPartysModel


class FoodComments(BaseModel): #评论属于哪个用户，哪个饭局
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="用户")
  food = models.ForeignKey(DinnerPartysModel, on_delete=models.CASCADE, verbose_name="饭局")
  comments = models.CharField(max_length=200, verbose_name="评论内容")

  class Meta:
    verbose_name = "课程评论"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.comments


class UserFavorite(BaseModel):
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="用户")
  fav_id = models.IntegerField(verbose_name="关注ID")
  fans_id = models.IntegerField(verbose_name='粉丝ID')

  class Meta:
    verbose_name = "用户收藏"
    verbose_name_plural = verbose_name

  def __str__(self):
    return "关注的用户ID:{fav}---粉丝的用户ID{fans}".format(fav=self.fav_id, fans=self.fans_id)


class UserMessage(BaseModel):
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="用户")
  message = models.CharField(max_length=200, verbose_name="消息内容")
  has_read = models.BooleanField(default=False, verbose_name="是否已读")

  class Meta:
    verbose_name = "用户消息"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.message
