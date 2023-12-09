from django.contrib import admin

from .models import Student, Teacher


class Student_teacher_inline(admin.TabularInline):
    model = Student.teachers.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','group']
    inlines = [Student_teacher_inline,]




@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','subject']
    inlines = [Student_teacher_inline,]
