from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Userinfo(models.Model):
    '''個人情報テーブル'''

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='氏名', max_length=128)
    sex = models.CharField(verbose_name='性別', max_length=128)
    # days = models.TimeField(verbose_name='日付', auto_now=False, auto_now_add=False)
    # days = models.DateTimeField(verbose_name='日付', default=timezone.now)
    age = models.IntegerField(verbose_name='年齢', null=False)
    info = models.CharField(verbose_name='情報', max_length=128)
    hobby = models.CharField(verbose_name='趣味', max_length=128)
    created_at = models.TimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.name


class SampleData(models.Model):
    '''サンプルテーブル'''

    id = models.BigIntegerField(primary_key=True)
    param_id = models.CharField(max_length=128)
    sample1 = models.CharField(max_length=128, null=False)
    sample2 = models.CharField(max_length=128, null=False)
    code1 = models.IntegerField(null=True, blank=True)
    code2 = models.IntegerField(null=True, blank=True)
    code3 = models.IntegerField(null=True, blank=True)
    code4 = models.IntegerField(null=True, blank=True)
    sample3 = models.CharField(max_length=128, null=True, blank=True)
    sample4 = models.CharField(max_length=128, null=True, blank=True)
    status = models.CharField(max_length=128, null=True, blank=True)
    delete_flag = models.IntegerField(null=True, blank=True)
    update_user = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.sample1


