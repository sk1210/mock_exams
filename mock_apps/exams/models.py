from django.db import models
import json
# Create your models here.

class QuestionType(models.Model):
    name = models.CharField(max_length=100, unique =True)
    def __str__(self):
        return self.name

class QuestionBank(models.Model):
    questiontype = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, unique =True)
    choices = models.CharField(max_length=200)
    correctChoice = models.IntegerField(default=0)


    def __str__(self):
        options = self.choices.split(",")
        answer = options[self.correctChoice]
        return str(self.questiontype) + " | " + self.text + " -> " +  ",".join(self.choices.split(",")) + " Answer: "  + answer


