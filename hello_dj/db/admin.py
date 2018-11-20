from django.contrib import admin

# Register your models here.
from .models import Department, Student, Stu_detail, Course


class DeptAdmin(admin.ModelAdmin):
    list_display = ['d_id', 'd_name']
    list_display_links = ['d_id', 'd_name']


class Stu_detailAdmin(admin.ModelAdmin):
    # fields = ['student', 'age', 'city']
    fieldsets = [
        ('一', {'fields': ['student']}),
        ('二', {'fields': ['age', 'city']}),
    ]


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 3


admin.site.register(Department, DeptAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Stu_detail, Stu_detailAdmin)
admin.site.register(Course)
