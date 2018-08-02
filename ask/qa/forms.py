from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        pass

    def save(self):
        quest = Question(**self.cleaned_data)
        quest.save()
        return quest

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean(self):
        pass
   
    def clean_question(self):
        quest_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=quest_id)
        except Question.DoesNotExist:
            question = None
        return question


    def save(self):
        ans = Answer(**self.cleaned_data)
        ans.save()


