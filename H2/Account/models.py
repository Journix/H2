from django.db import models
from django.contrib.auth.models import Group, User
import  mongoengine as mongo

#### Mongo DB Test
# class UserProfile(mongo.Document):
#     pass

class UserProfile(models.Model):
    user_id = models.CharField(default=0,max_length=100)#所属用户id
    nickname = models.CharField(max_length=64, null=True)#昵称
    account_type = models.CharField(max_length=10,default="USER")#账户类型
    avatar = models.URLField(default='/static/img/default_avatar.jpg')#头像
    signature = models.CharField(max_length = 140, null=True)#签名
    phone = models.CharField(max_length = 20, null=True)#手机
    remark = models.TextField(max_length=256, null=True)#备注
    created_at = models.DateTimeField(auto_now_add=True, null=True)#创建时间

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = "account_user_profile"
        verbose_name = "用户资料"
        ordering = ['-created_at']

