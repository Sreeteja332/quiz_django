from django.db import models    
from django.contrib.auth.models import User
import uuid
import random

class Exam(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    corrans = models.CharField(max_length=100)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "Questions"

class QuizResult(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    score = models.PositiveIntegerField(blank=True,null=True)
    date_taken = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f"{self.user}, {self.score}"