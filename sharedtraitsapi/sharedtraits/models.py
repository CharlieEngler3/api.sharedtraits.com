from django.db import models

class UserAnswerModel(models.Model):
    username = models.CharField(max_length=20)
    questionID = models.IntegerField(default=-1)
    answer = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class QuestionModel(models.Model):
    question = models.TextField()
    answers = models.TextField()