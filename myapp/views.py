from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.forms import StudentSignupForm,TeacherSignUpForm
from myapp.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from myapp.decorators import student_required,teacher_required

from django.views.generic import CreateView



class StudentSignUpView(CreateView):
    model=User
    form_class=StudentSignupForm
    template_name='myapp/StudentRegistration.html'
    def get_context_data(self,**kwargs):
        kwargs['user_type']='student'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
            if form.is_valid():
                user=form.save()
                login(self.request,user)
                return HttpResponseRedirect('/login/')
class TeacherSignUpView(CreateView):
    model=User
    form_class=TeacherSignUpForm
    template_name='myapp/TeacherRegistration.html'

    def get_context_data(self,**kwargs):
        kwargs['user_type']='teacher'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        if form.is_valid():
            user=form.save()
            login(self.request,user)
            return HttpResponseRedirect('/login/')

@login_required
@student_required
def Home(request):
    context={

    }
    return render(request,'myapp/home.html',context)
