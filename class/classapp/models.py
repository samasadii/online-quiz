from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ClassRoom(models.Model):
    admin = models.ManyToManyField('UserProfile', related_name="managing")
    student = models.ManyToManyField('UserProfile', blank=True, related_name="classes")

    address = models.CharField(max_length=225)
    name = models.CharField(max_length=225)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    @property
    def token(self):
        token, created = Token.objects.get_or_create(user=self.user)
        return token.key


class Question(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=500)

    number = models.IntegerField()


class Exam(models.Model):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="exams")

    title = models.CharField(max_length=225)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class ExamAnswer(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="exam_answers")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="answers")


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    exam_answer = models.ForeignKey('ExamAnswer', on_delete=models.CASCADE, related_name="answers")

    text = models.CharField(max_length=500)
