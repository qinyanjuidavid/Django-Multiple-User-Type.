from django.urls import path
from django.contrib.auth import views as auth_views
from myapp.views import StudentSignUpView,TeacherSignUpView
from myapp import views
app_name='myapp'

urlpatterns=[
path('',StudentSignUpView.as_view(),name='register'),
path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
path('teacher/',TeacherSignUpView.as_view(),name='teacherRegister'),
#path('',views.Registration,name='register'),
path('home/',views.Home,name="home")
]
