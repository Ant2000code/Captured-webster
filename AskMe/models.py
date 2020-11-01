from django.db import models


class Detail(models.Model):
    category=models.CharField(max_length=10)
    userName=models.CharField(max_length=50,default="")
    #qualification=models.ChoiceField()
    quesNo=models.IntegerField(default=0)
    ansNo=models.IntegerField(default=0)
    profilepic=models.ImageField(upload_to='pictures',default="",blank=True,null=True)
    workingOn=models.IntegerField(default=0)

def __str__(self): 
         return ""+self.userName

class Question(models.Model):
    topic=models.CharField(max_length=300,default="")
    quesText=models.CharField(max_length=300,default="")
    time=models.DateTimeField(auto_now_add=True)
    postedBy=models.CharField(max_length=50,default="",null=False,blank=False)
    accepted=models.BooleanField(default=False)
    acceptedBy=models.CharField(max_length=50, default="",null=False,blank=True)
    answered=models.BooleanField(default=False)
    expired=models.BooleanField(default=False)
    quesImg=models.ImageField(upload_to='quesimages',default="",blank=True,null=True)
    rating=models.IntegerField(default=0)
    attachment=models.FileField(upload_to='quesfiles',default="",blank=True,null=True)
    
     
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    ansText=models.TextField()
    answeredBy=models.CharField(max_length=50,default="",null=False,blank=False)
    time=models.DateTimeField(auto_now_add=True)
    ansImg=models.ImageField(upload_to='ansimages',default="",blank=True,null=True)
    rating=models.IntegerField(default=0)
    attachment=models.FileField(upload_to='ansfiles',default="",blank=True,null=True)
    
class AnsComment(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    comment_text=models.TextField()
    posted_by=models.CharField(max_length=100,default="",null=False,blank=False)
    time=models.DateTimeField(auto_now_add=True)

class QuesComment(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='ques_comment')
    comment_text=models.TextField()
    posted_by=models.CharField(max_length=100,default="",null=False,blank=False)
    time=models.DateTimeField(auto_now_add=True)


    

