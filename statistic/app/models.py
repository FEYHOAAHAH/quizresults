from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Questions(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    correct_answers_count = models.PositiveIntegerField()
    incorrect_answers_count = models.PositiveIntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    date_answered = models.DateTimeField(auto_now_add=True)
