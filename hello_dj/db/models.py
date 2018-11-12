from django.db import models


# Create your models here.

class Department(models.Model):
    """
    学院信息
    """
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30)

    def __str__(self):
        return f'Department<d_id={self.d_id},d_name={self.d_name}>'


class Student(models.Model):
    """
    学生信息 多对一
    """
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)
    # on_delete  级联删除 如果学院信息删除了 那么对应的学生信息也删除
    # dept_id
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f'Student<s_id={self.s_id},s_name={self.s_name},dept_id={self.dept_id}>'


class Course(models.Model):
    """
    课程信息 多对多
    """
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30)
    student = models.ManyToManyField('Student')

    # 帮我们自动生成关系表
    def __str__(self):
        return f'Course<c_id={self.c_id},c_name={self.c_name}>'


class Stu_detail(models.Model):
    """
    学生的详细信息 一对一
    """
    # studet_id 关联Student
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.BooleanField(default=1)
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'Stu_detail<s_id={self.student},age={self.age},gender={self.gender},city={self.city}>'
