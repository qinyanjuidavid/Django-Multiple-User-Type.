from django.contrib import admin
from myapp.models import User, Student,Subject,Lesson,Teacher


admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Teacher)
