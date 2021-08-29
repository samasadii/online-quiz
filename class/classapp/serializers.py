from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils.crypto import get_random_string

from .models import UserProfile, ClassRoom, Exam, Question, ExamAnswer, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'password', 'username']
        extra_kwargs = {"password": {"write_only": True}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'token']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data.pop('user'))
        user_profile = UserProfile(**validated_data, user=user)
        user_profile.save()
        return user_profile


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ExamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ClassRoomExamsRetrieveSerializer(serializers.ModelSerializer):
    exams = ExamRetrieveSerializer(read_only=True, many=True)

    class Meta:
        model = ClassRoom
        fields = ['id', 'exams', 'name', 'address']


class ClassRoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'address', 'admin', 'student']
        extra_kwargs = {"address": {"read_only": True}, "student": {"read_only": True}}

    def create(self, validated_data):
        address = get_random_string(length=32)
        admin = validated_data.pop('admin')[0]
        class_room = ClassRoom(**validated_data, address=address)
        class_room.save()
        class_room.admin.add(admin)
        return class_room


class ClassRoomRetrieveSerializer(serializers.ModelSerializer):
    student = UserProfileSerializer(read_only=True, many=True)
    admin = UserProfileSerializer(read_only=True, many=True)

    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'address', 'admin', 'student']


class ExamSerializer(serializers.ModelSerializer):
    questions = serializers.ListField(write_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'start_time', 'end_time', 'class_room', 'questions']

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        exam = Exam.objects.create(**validated_data)
        for question in questions:
            Question.objects.create(exam=exam, **question)
        return exam


class AnswerSerializer(serializers.ModelSerializer):
    answers = serializers.ListField(write_only=True)

    class Meta:
        model = ExamAnswer
        fields = ['id', 'user_profile', 'exam', 'answers']

    def create(self, validated_data):
        answers = validated_data.pop('answers')
        exam_answer = ExamAnswer.objects.create(**validated_data)
        for answer in answers:
            question = Question.objects.get(id=answer.pop('question'))
            Answer.objects.create(exam_answer=exam_answer, question=question, **answer)
        return exam_answer
