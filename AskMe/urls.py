
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', views.home, name='home'),
    path('home/Science',views.home2,name='home2'),
    path('home/SocialScience',views.home3,name='home3'),
    path('home/LanguageAndLiterature',views.home4,name='home4'),
    path('home/Miscellaneous',views.home5,name='home5'),
    path("register/tutor", views.registerTutor,name="registertutor"),
    path("register/student", views.registerStudent, name="registerstudent"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/question', views.Askquestion, name='question'),
    path('dashboard/answer/<int:id>', views.answer, name='answer'),
    path('dashboard/Answer/<int:id>', views.answer2, name='answer'),
    path('dashboard/save/<int:id>',views.dashboard2,name='dashboard2'),
    path('dashboard/settings',views.settingS,name='settingS'),
    path('solution/<int:id>', views.solution, name='solution'),
    path('savecomment',views.savecomment,name='savecomment'),
    path('rate1/<int:id>',views.Rate1,name='Rate1'),
    path('rate2/<int:id>',views.Rate2,name='Rate2'),
    path('rate3/<int:id>',views.Rate3,name='Rate3'),
    path('rate4/<int:id>',views.Rate4,name='Rate4'),
    path('rate5/<int:id>',views.Rate5,name='Rate5'),
    path('savecommentques',views.savecomment2,name='savecomment2'),
    path('solution/logout', views.logout, name='logout')
    ]
   
    


    
    

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

