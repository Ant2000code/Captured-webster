
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', views.home, name='home'),
    path("register/tutor", views.registerTutor,name="registertutor"),
    path("register/student", views.registerStudent, name="registerstudent"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/question', views.Askquestion, name='question'),
    path('dashboard/answer/<int:id>', views.answer, name='answer'),
    path('home/solution/<int:id>', views.solution, name='solution'),
    path('home/solution/logout', views.logout, name='logout')
    ]
   
    
