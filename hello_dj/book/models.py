from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)  # 自增长,可以省略
    name = models.CharField(max_length=30)  # char类型最大长度30
    age = models.IntegerField()  # Int类型
    city = models.CharField(max_length=100,null='浙江') #设置为空
    note = models.CharField(max_length=100,null=True) #设置为空


    def __str__(self):
        return f"User<id={self.id}, name={self.name}, age={self.age}>"


# class Test1(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()

# 配置连接
# 创建模型类
# 创建映射文件 makemigrations
# 生成数据表 migrate


class F_test(models.Model):
    name = models.CharField(max_length=30,unique=True)
    age = models.IntegerField()
    note = models.TextField(null=True)
    gender = models.BooleanField(default=True)
    #第一次的时间，更新不修改
    create_time = models.DateField(auto_now_add=True)
    #实时修改
    update_time = models.DateTimeField(auto_now=True)
