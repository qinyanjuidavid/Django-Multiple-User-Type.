from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from myapp.models import User,Student,Subject,Lesson,Teacher

class StudentSignupForm(UserCreationForm):
    interests=forms.ModelMultipleChoiceField(
    queryset=Subject.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True
    )
    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_student=True
        user.save()
        student=Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user

class TeacherSignUpForm(UserCreationForm):
    preference=forms.ModelMultipleChoiceField(
    queryset=Lesson.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True
    )
    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self,commit=False):
        user=super().save(commit=False)
        user.is_teacher=True
        user.save()
        teacher=Teacher.objects.create(user=user)
        teacher.preference.add(*self.cleaned_data.get('preference'))
        return user
