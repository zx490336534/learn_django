from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)  # 自增长,可以省略
    name = models.CharField(max_length=30)  # char类型最大长度30
    age = models.IntegerField()  # Int类型

    def __str__(self):
        return f"User<id={self.id}, name={self.name}, age={self.age}>"


class Test1(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

# 配置连接
# 创建模型类
# 创建映射文件 makemigrations
# 生成数据表 migrate
