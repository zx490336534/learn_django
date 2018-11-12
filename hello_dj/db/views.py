from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Department, Student, Stu_detail, Course


def test(request):
    # d1 = Department(d_name='文学院')
    # d1.save()
    # s1 = Student(s_name='小皮',dept_id=1)
    # s1.save()
    s1 = Student.objects.get(s_id=1)  # 学生的实例对象
    d1 = Department.objects.get(d_id=1)  # 学院的实例对象
    print(s1)
    print(s1.s_name)
    print(s1.dept_id)
    print(s1.dept)
    print(d1)
    print(d1.d_name)
    print(d1.student_set)  # db.Student.None
    # 反向查询的时候的一种管理器里面包含了方法
    print(d1.student_set.all())  # .all拿到数据
    d2 = Department.objects.get(d_id=2)
    # add()方法，一对多，多对多 添加数据 修改 数据已经存在
    # d2.student_set.add(s1) #给s1学生换学院
    # create() 方法 一对多，多对多  添加没有存在的数据 新建
    d2.student_set.create(s_name='李易峰')
    # remove()方法 多对多（会约束）

    return HttpResponse('XXX')


def test22(request):
    # 插入数据
    # Department.objects.create(d_name='语言学院')
    # s1 = Student(s_name='小明',dept_id=2)
    # s1.save()
    # s2 = Student(s_name='小红')
    # department = Department.objects.get(d_id=3)
    # s2.dept = department
    # s2.save()
    # 往详细表添加数据
    # std1 = Stu_detail(student_id=2,age=22,gender=1,city='shanghai')
    # std1.save()
    # 往课程表中加数据
    # py = Course(c_name='python')
    # py.save()
    # java = Course(c_name='java')
    # java.save()
    ruanjian = Department.objects.get(d_id=1)  # 学院的第一条数据的实例对象
    zx = Student.objects.get(s_id=1)  # 学生的一个实例对象
    stu_detail1 = Stu_detail.objects.get(id=1)  # 详细的一个实例对象
    python = Course.objects.get(c_id=1)  # 课程的一个实例对象
    java = Course.objects.get(c_name='java')  # 课程的一个实例对象
    """关联对象的访问"""
    # 正向查询 .属性
    # 方向查询 .类名小写_set
    # 一对多
    print('一对多')
    print(zx.dept)  # 学生的所属学院
    print(ruanjian.student_set.all())  # 属于这个学院的所有学生
    # 一对一
    print('一对一')
    print(stu_detail1.student)
    print(zx.stu_detail)
    # 多对多
    print('多对多')
    print(python.student)  # 报名这个课程的所有学生
    print(zx.course_set.all())  # 学生报名的课程

    """表关联对象的方法"""
    """add(),一对多，多对多，数据已经存在于数据库"""
    # wen = Department.objects.get(d_id=3)
    # print('修改学院为文学院：')
    # wen.student_set.add(zx)
    # zx.course_set.add(python)
    # print('报名的课程：',zx.course_set.all())
    # zx.course_set.add(python,java)
    # """create(), 数据不存在 新建 一对多 多对多"""
    # wen.student_set.create(s_name='叶子')
    # ruanjian.student_set.create(s_name='张林林')
    # "python课程新加入了一个学生，同时将信息录入了两张表"
    # python.student.create(s_name='陈皮皮',dept_id=2)
    # zx.course_set.create(c_name='日语')
    # """remove() 多对多"""
    # python.student.remove(zx)
    """clear()"""
    python.student.clear()  # 删除全部python课程
    return HttpResponse('XXX')


def test3(request):
    """多表查询"""
    # 查询学院名字为"软件学院"的学生的信息
    rs = Student.objects.filter(dept__d_name='软件学院')
    print(rs)
    # 查询学生名字中包含'小'字的学生的学院信息
    rs = Department.objects.filter(student__s_name__contains='小')
    print(rs)
    # 查询学号为1的学生所有的课程
    rs = Course.objects.filter(student__s_id=1)
    print(rs)
    # 报名了java课程的所有学生
    rs = Student.objects.filter(course__c_name='java')
    print(rs)
    # 查询了报名了python课程的学生的所属的学院的信息
    rs = Department.objects.filter(student__course__c_name='python')
    print(rs)

    return HttpResponse('XXX')
