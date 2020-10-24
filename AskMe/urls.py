
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('home',views.home, name='home'),
    path('home/Science',views.home2,name='home2'),
    path('home/SocialScience',views.home3,name='home3'),
    path('home/LanguageAndLiterature',views.home4,name='home4'),
    path('home/Miscellaneous',views.home5,name='home5'),
    path("register/tutor",views.registerTutor,name="registertutor"),
    path("register/student",views.registerStudent,name="registerstudent"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/question',views.Askquestion,name='question'),
    path('dashboard/answer/<int:id>',views.answer,name='answer'),
    path('dashboard/save/<int:id>',views.dashboard2,name='dashboard')
    
    
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)