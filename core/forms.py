from django import forms
from django.contrib.auth.models import User


class BlogForm(forms.Form):
    title = forms.CharField()
    message = forms.CharField()


class QuestionForm(forms.Form):
    questiontitle = forms.CharField()
    questiondetails = forms.CharField()


class AnswerForm(forms.Form):
    answer = forms.CharField()


class CommentForm(forms.Form):
    comment = forms.CharField()
