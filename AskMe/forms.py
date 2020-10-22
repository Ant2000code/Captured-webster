from django.forms import ModelForm
from .models import Answer, Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('quesText', 'quesImg')


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('ansText', 'ansImg')
