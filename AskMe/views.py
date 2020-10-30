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
from django.conf import settings
from django.core.mail import send_mail
import json


# Create your views here.
def home(request):
 if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(quesText__icontains=search).order_by('-id')
 else:    
       que=Question.objects.all().order_by('-id')
       
 return render(request,'index.html',{'que':que})

def solution(request, id):
    que = Question.objects.get(pk=id)
    ans = Answer.objects.get(question=que)
    AnsC=AnsComment.objects.filter(answer=ans)
    QuesC=QuesComment.objects.filter(question=que)
    return render(request, 'solution.html', {'ans': ans, 'que': que,'AnsC':AnsC,'QuesC':QuesC})

# Save Answer Comment method
def savecomment(request):
    if request.method=='POST':
        comment_text=request.POST['comment']
        ansid=request.POST['ans_id']
        answer=Answer.objects.get(pk=ansid)
        posted_by=request.user.username
        recip=answer.answeredBy
        recipient=User.objects.get(username=recip)
        bool=True
        AnsComment.objects.create(
            comment_text=comment_text,
            answer=answer,
            posted_by=posted_by

        )
        subject ='New comment!'
        message = f'Hi {answer.answeredBy}, Someone commented on your answer to {answer.question.quesText}!'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [recipient.email, ] 
        send_mail( subject, message, email_from, recipient_list )


    return HttpResponse(json.dumps({'commment':comment_text,'ansid':ansid,'postedby':posted_by,'bool':True}), content_type="application/json")
    #return JsonResponse({'bool':True})

# Save comment on Question 
def savecomment2(request):
    if request.method=='POST':
        comment_text=request.POST['comment']
        quesid=request.POST['ques_id']
        question=Question.objects.get(pk=quesid)
        posted_by=request.user.username
        recip=question.postedBy
        recipient=User.objects.get(username=recip)
        bool=True
        QuesComment.objects.create(
            comment_text=comment_text,
            question=question,
            posted_by=posted_by

        )
        subject ='New comment!'
        message = f'Hi {question.postedBy}, Someone commented on your question {question.quesText}!'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [recipient.email, ] 
        send_mail( subject, message, email_from, recipient_list )



    return HttpResponse(json.dumps({'commment':comment_text,'quesid':quesid,'postedby':posted_by,'bool':True}), content_type="application/json")   

#Filter topic Science
def home2(request):
    if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Science",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Science").order_by('-id')
    return render(request,'index.html',{'que':que})

#Filter topic Social Science
def home3(request):
    if 'search' in request.GET:
        search=request.GET['search']
        que=Question.objects.filter(topic="Social Science",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Social Science").order_by('-id')
    return render(request,'index.html',{'que':que})

#Fiter topic Language and Literature
def home4(request):
    if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Language and Literature",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Language and Literature").order_by('-id')
    return render(request,'index.html',{'que':que})

#Filter topic Miscellaneous
def home5(request):
    if 'search' in request.GET:
        search=request.GET['search']
        
        que=Question.objects.filter(topic="Miscellaneous",quesText__icontains=search).order_by('-id')
    else:
        que=Question.objects.filter(topic="Miscellaneous").order_by('-id')
    return render(request,'index.html',{'que':que})



#Login 
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

#Register Tutor
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
                return redirect('/register/tutor')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/register/tutor') 
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
            return redirect('/register/tutor')
        return redirect('/home')
    else:
        return render(request,'register.html')

#registration of student
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
                return redirect('/register/student')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/register/student') 
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
            messages.info(request, 'password not matching..')
            return redirect('/register/student')
        return redirect('/home')
    else:
        return render(request,'register.html')

#logout
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
        que2=Question.objects.filter(answered=True,acceptedBy=curruser).order_by('-id')
        workOn=det.workingOn
        print(workOn)
        return render(request,'Tdashboard.html',{'que':que,'workOn':workOn,'det':det,'que2':que2})
 else:
        que2=Question.objects.filter(answered=False,expired=False,postedBy=curruser).order_by('-id')
        que3=Question.objects.filter(answered=True,postedBy=curruser).order_by('-id')
        que4=Question.objects.filter(expired=True,postedBy=curruser).order_by('-id')
        return render(request,'Sdashboard.html',{'det':det,'que2':que2,'que3':que3})

#This function is called when tutor clicks on Accept and Save
def dashboard2(request,id):
    que=Question.objects.get(pk=id)
    now=datetime.utcnow().replace(tzinfo=utc)
    timediff = now-que.time
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
         subject = 'Question accepted and saved!'
         message = f'Hi {curruser}, You saved question: {que.quesText}. You can check your current working question in your dashboard. Answer it within 24 hours or it will expire!'
         email_from = settings.EMAIL_HOST_USER 
         recipient_list = [request.user.email, ] 
         send_mail( subject, message, email_from, recipient_list )
         print(que.quesText)
         return redirect('dashboard')
      else:
         return redirect('dashboard')
    
   #Get user settings
def settingS(request):
    curruser=request.user.username
    det=Detail.objects.get(userName=curruser)
    if request.method =='POST':
       img=request.FILES['profilepicture']
       det.profilepic=img
       det.save(update_fields=["profilepic"])
       return redirect('/dashboard/settings')
    else:
       return render(request,'userSettings.html',{'det':det})     
        


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
        subject = 'You asked a Question!'
        message = f'Hi {curruser}, You asked question: {quesText}. Your question will soon be accepted by our Tutors! Thank You for trusting us!'
        
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [request.user.email, ] 
        send_mail( subject, message, email_from, recipient_list )
        return redirect('dashboard')

    else: 
      return render(request,'question.html',{'form':form})


#When Answer is called directly
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
        que.acceptedBy=curruser
        que.answered=True
        que.save(update_fields=["accepted"])
        que.save(update_fields=["answered"])
        que.save(update_fields=["acceptedBy"])
        que.save(update_fields=["answered"])
        ans.save()
        subject ='You Answered!'
        message = f'Hi {curruser}, You answered question: {que.quesText}. All the best for future!'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [request.user.email, ] 
        send_mail( subject, message, email_from, recipient_list )
        return redirect('dashboard')

    else:

       queId=Question.objects.get(pk=id)
       now=datetime.utcnow().replace(tzinfo=utc)
       timediff = now -queId.time
       tf=timediff.total_seconds()>86400 #check 24 hour timer
       curruser=request.user.username
       det=Detail.objects.get(userName=curruser)
       if tf==True:
         queId.expired=True
         queId.save(update_fields=['expired'])
         det.workingOn=0
         det.save(update_fields=['workingOn'])
         return redirect('dashboard')
       else:
           if det.workingOn==0:
              return render(request, 'answer.html',{'queId':queId})
           else:
              return redirect('dashboard')


 #Answer page from already saved section
def answer2(request,id):

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
        que.acceptedBy=curruser
        que.answered=True
        que.save(update_fields=["accepted"])
        que.save(update_fields=["answered"])
        que.save(update_fields=["acceptedBy"])
        que.save(update_fields=["answered"])
        ans.save()
        subject ='You Answered!'
        message = f'Hi {curruser}, You answered question: {que.quesText}. All the best for future!'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [request.user.email, ] 
        send_mail( subject, message, email_from, recipient_list )
        return redirect('dashboard')

    else:

       queId=Question.objects.get(pk=id)
       now=datetime.utcnow().replace(tzinfo=utc)
       timediff = now -queId.time
       tf=timediff.total_seconds()>86400 #check 24 hour timer
       curruser=request.user.username
       det=Detail.objects.get(userName=curruser)
       if tf==True:
         queId.expired=True
         queId.save(update_fields=['expired'])
         det.workingOn=0
         det.save(update_fields=['workingOn'])
         return redirect('dashboard')
       else:
           if det.workingOn>0:
              return render(request, 'answer.html',{'queId':queId})
           else:
              return redirect('dashboard')



