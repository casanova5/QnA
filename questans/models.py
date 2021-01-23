import datetime
from django.db import models
from django.utils import timezone
#from taggit.managers import TaggableManager


class Question(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='q_by_u', null=True, blank=True)
    question_name = models.CharField(max_length=80, default='')
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
#   tags = TaggableManager()
    
    def __str__(self):
        return self.question_name
    
    
class Answer(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='a_by_u')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text