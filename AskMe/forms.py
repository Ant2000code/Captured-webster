from django.forms import ModelForm
from .models import Answer,Question

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('quesText','quesImg')