from django import forms
from qa.models import Question, Answer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('No username info')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('There is user with the same login')
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('No email info')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('No password info')
        return password

    def save(self):
        user = User.objects.create_user(self.cleaned_data.get('username'), self.cleaned_data.get('email'), self.cleaned_data.get('password'))
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('No username info')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('No password info')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('wrong login-password')
        if not user.check_password(password):
            raise forms.ValidationError('wrong login-password')

