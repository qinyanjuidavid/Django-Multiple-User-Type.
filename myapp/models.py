from django.db import models
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Lesson(models.Model):
    name_l=models.CharField(max_length=20)

    def __str__(self):
        return self.name_l
class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    interests=models.ManyToManyField(Subject)

    def __str__(self):
        return self.user.username
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    preference=models.ManyToManyField(Lesson)

    def __str__(self):
        return self.user.username
