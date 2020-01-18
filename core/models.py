from django.db import models
from django.conf import settings
from django.utils import timezone


class Blog(models.Model):
    username = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    datetime = models.DateTimeField(default=timezone.now)
    # blog id
    # like

    def __str__(self):
        return self.title


class Rank(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Question_cat(models.Model):
    c_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100) 


class Question(models.Model):
    username = models.CharField(max_length=100, default='')
    questiontitle = models.CharField(max_length=100, default='')
    questiondetails = models.TextField(max_length=500, default='')
    qid = models.AutoField(primary_key=True)
    #c_id = models.ForeignKey(Question_cat, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.questiontitle


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer


class Comment(models.Model):
    username = models.CharField(max_length=100)
    aid = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    cid = models.IntegerField(null=True)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
