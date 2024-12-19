'''Database schema'''
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    '''Question schema'''
    question_tpy = models.CharField(max_length=200)
    Pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_tpy
    def was_published_recently(self):  # noqa
        '''Published date'''
        return self.Pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    '''Choice schema'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt
