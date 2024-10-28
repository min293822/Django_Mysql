from django.contrib import admin
from .models import Subject, Teacher, Student, Headmaster, Class, Exam

class SubjectAdmin(admin.ModelAdmin):
  list_display = ['name', 'grade', 'total_chapter']
  
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name', 'grade', 'age', 'gender']

class ExamAdmin(admin.ModelAdmin):
  list_display = ['grade', 'max_point', 'subject', 'date']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Teacher)
admin.site.register(Headmaster)
admin.site.register(Class)
