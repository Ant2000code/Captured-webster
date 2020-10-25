from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth
from django.db.models import Count, F, Value
from .forms import QuestionForm
from django.conf import settings 
from django.core.mail import send_mail


# Create your views here.
def home(request):
    que=Question.objects.all().order_by('-id')
    return render(request,'index.html',{'que':que})



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def registerTutor(request):

    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        category='Tutor'


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register/tutor')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register/tutor') 
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                detail=Detail.objects.create(
                category=category,
                userName=username,
                quesNo=0,
                ansNo=0
                )
                detail.save()
                 
                subject = 'Registration done successfully'
                message = f'Hi {user.username}, thank you for registering in Ask me Anything.'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [user.email, ] 
                send_mail( subject, message, email_from, recipient_list )
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')
            return redirect('register/tutor')
        return redirect('/home')
    else:
        return render(request,'register.html')

def registerStudent(request):

    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        category='Student'


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register/student')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register/student') 
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                detail=Detail.objects.create(
                category=category,
                userName=username,
                quesNo=0,
                ansNo=0
                )
                detail.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')
            return redirect('register/student')
        return redirect('/home')
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/home')


def dashboard(request):
    curruser=request.user.username
    det=Detail.objects.get(userName=curruser)
    cate=det.category
    print(cate)
    if cate =='Tutor':
        que=Question.objects.all().order_by('-id')
        
        return render(request,'Tdashboard.html',{'que':que})
    else:
        return render(request,'Sdashboard.html')

def Askquestion(request):
    form=QuestionForm
    if request.method == 'POST':
        quesText=request.POST['questxt']
        quesImg=request.POST['image']
        topic=request.POST['topic']
        postedBy=request.user.username
        curruser=request.user.username
        det=Detail.objects.get(userName=curruser)
        
        question=Question.objects.create(
            topic=topic,
            quesText=quesText,
            postedBy=postedBy,
            quesImg=quesImg
        )
        det.quesNo=F('quesNo')+1
        det.save(update_fields=["quesNo"])
        question.save()
        return redirect('dashboard')

    else: 
      return render(request,'question.html',{'form':form})

def answer(request,id):
    if request.method=='POST':
        ansText=request.POST['answertxt']
        ansImg=request.POST['image']
        answeredBy=request.user.username
        curruser=request.user.username
        det=Detail.objects.get(userName=curruser)
        que=Question.objects.get(pk=id)

        ans=Answer.objects.create(
            question=que,
            ansText=ansText,
            answeredBy=answeredBy,
            ansImg=ansImg
        )
        det.ansNo=F('ansNo')+1
        det.save(update_fields=["ansNo"])
        que.accepted=True
        que.acceptedBy=curruser
        que.save(update_fields=["accepted"])
        que.save(update_fields=["acceptedBy"])
        ans.save()
        return redirect('dashboard')

    else:
       queId=Question.objects.get(pk=id)
       return render(request, 'answer.html',{'queId':queId})



# Adding questions according to topic 

def science(request):
    que=Question.objects.all().order_by('-id')
    return render(request,'science.html',{'que':que})

def Social(request):
    que=Question.objects.all().order_by('-id')
    return render(request,'Social.html',{'que':que})

def Language(request):
    que=Question.objects.all().order_by('-id')
    return render(request,'Language.html',{'que':que})

def Miss(request):
    que=Question.objects.all().order_by('-id')
    return render(request,'Miss.html',{'que':que})