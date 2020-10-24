from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth
from django.db.models import Count, F, Value
from .forms import QuestionForm
from datetime import datetime,date
from django.utils.timezone import utc



# Create your views here.
def home(request):
 if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Science",quesText__icontains=search).order_by('-id')
 else:    
       que=Question.objects.all().order_by('-id')
       ans=Answer.objects.all().order_by('id')
 return render(request,'index.html',{'que':que, 'ans':ans})

def solution(request, id):
    que = Question.objects.get(pk=id)
    ans = Answer.objects.get(question=que)
    return render(request, 'solution.html', {'ans': ans, 'que': que})

    if 'search' in request.GET:
        search=request.GET['search']
        que=Question.objects.filter(quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.all().order_by('-id')
        
    return render(request,'index.html',{'que':que})


def home2(request):
    if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Science",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Science").order_by('-id')
    return render(request,'index.html',{'que':que})

def home3(request):
    if 'search' in request.GET:
        search=request.GET['search']
        que=Question.objects.filter(topic="Social Science",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Social Science").order_by('-id')
    return render(request,'index.html',{'que':que})

def home4(request):
    if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Language and Literature",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Language and Literature").order_by('-id')
    return render(request,'index.html',{'que':que})

def home5(request):
    if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Miscellaneous",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Miscellaneous").order_by('-id')
    return render(request,'index.html',{'que':que})



def answersave(request):
    return render(request,'ajaxtest.html')

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

                category=category,
                userName=username,
                quesNo=0,
                ansNo=0
                
                detail.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'password not matching..')
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
        workOn=det.workingOn
        print(workOn)
        return render(request,'Tdashboard.html',{'que':que,'workOn':workOn,'det':det})
 else:
        return render(request,'Sdashboard.html')

def dashboard2(request,id):
    que=Question.objects.get(pk=id)
    now=datetime.utcnow().replace(tzinfo=utc)
    timediff = now -que.time
    tf=timediff.total_seconds()>86400
    curruser=request.user.username
    det=Detail.objects.get(userName=curruser)
    if tf==True:
         que.expired=True
         que.save(update_fields=['expired'])
         return redirect('dashboard')
    else:
      if det.workingOn==0:
         que.accepted=True
         curruser=request.user.username
         que.acceptedBy=curruser
         que.save(update_fields=["accepted"])
         que.save(update_fields=["acceptedBy"])
         det=Detail.objects.get(userName=curruser)
         det.workingOn=id
         det.save(update_fields=['workingOn'])
         print(que.quesText)
         return redirect('dashboard')
      else:
         return redirect('dashboard')
    
        
        


def Askquestion(request):
    form=QuestionForm
    if request.method == 'POST':
        quesText=request.POST['questxt']
        quesImg=request.POST['image']
        topic=request.POST['topic']
        postedBy=request.user.username
        curruser=request.user.username
        det=Detail.objects.get(userName=curruser)
        

        question=Question.objects.create\
                (

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
        det.workingOn=0
        det.save(update_fields=['workingOn'])
        det.save(update_fields=["ansNo"])
        que.accepted=True

        que.answered=True
        que.acceptedBy=curruser
        que.answered=True
        que.save(update_fields=["accepted"])
        que.save(update_fields=["answered"])
        que.save(update_fields=["acceptedBy"])
        que.save(update_fields=["answered"])
        ans.save()
        return redirect('dashboard')

    else:

       queId=Question.objects.get(pk=id)
       now=datetime.utcnow().replace(tzinfo=utc)
       timediff = now -queId.time
       tf=timediff.total_seconds()>86400
       curruser=request.user.username
       det=Detail.objects.get(userName=curruser)
       if tf==True:
         queId.expired=True
         queId.save(update_fields=['expired'])
         return redirect('dashboard')
       else:
           if det.workingOn==0:
              return render(request, 'answer.html',{'queId':queId})
           else:
              return redirect('dashboard')

           


