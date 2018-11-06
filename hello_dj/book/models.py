from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)  # 自增长,可以省略
    name = models.CharField(max_length=30)  # char类型最大长度30
    age = models.IntegerField()  # Int类型
