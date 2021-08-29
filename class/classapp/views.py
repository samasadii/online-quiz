from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from classapp.models import UserProfile, ClassRoom, Exam
from classapp.serializers import UserProfileSerializer, AuthSerializer, ClassRoomCreateSerializer, \
    ClassRoomRetrieveSerializer, ExamSerializer, AnswerSerializer, ExamRetrieveSerializer, QuestionSerializer, \
    ClassRoomExamsRetrieveSerializer


class CreateClassRoom(CreateAPIView):
    serializer_class = ClassRoomCreateSerializer


class CreateExam(CreateAPIView):
    serializer_class = ExamSerializer


class CreateUser(CreateAPIView):
    serializer_class = UserProfileSerializer


class TakeExam(CreateAPIView):
    serializer_class = AnswerSerializer


class Authentication(APIView):
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data.get('username'))
            if user.check_password(request.data.get('password')):
                profile = user.user_profile
                profile_serializer = UserProfileSerializer(instance=profile)
                return Response(profile_serializer.data)
            raise User.DoesNotExist
        except User.DoesNotExist:
            return Response({'error': 'Invalid Username or Password'}, status=400)


class RetrieveUserClassRooms(APIView):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, id=kwargs.get('user_id'))
        admin = ClassRoomRetrieveSerializer(instance=user.managing.all(), many=True)
        student = ClassRoomRetrieveSerializer(instance=user.classes.all(), many=True)
        data = {'admin': admin.data, 'membership': student.data}
        return Response(data, status=200)


class RetrieveExamQuestions(APIView):

    def get(self, request, *args, **kwargs):
        exam = get_object_or_404(Exam, id=kwargs.get('exam_id'))
        questions = exam.questions
        exam = ExamRetrieveSerializer(instance=exam).data
        questions = QuestionSerializer(instance=questions, many=True).data
        return Response({'exam': exam, 'questions': questions}, status=200)


class RetrieveClassRoomExams(RetrieveAPIView):
    serializer_class = ClassRoomExamsRetrieveSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'


class RetrieveClassRoom(RetrieveAPIView):
    serializer_class = ClassRoomRetrieveSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'class_pk'


class JoinClassRoom(APIView):
    def post(self, request, *args, **kwargs):
        class_room = get_object_or_404(ClassRoom, address=kwargs.get('address'))
        user_profile = get_object_or_404(UserProfile, id=kwargs.get('user_id'))
        class_room.student.add(user_profile)
        class_room = ClassRoomRetrieveSerializer(instance=class_room)
        return Response(class_room.data, status=200)


class AddAdminToClassRoom(APIView):
    def post(self, request, *args, **kwargs):
        class_room = get_object_or_404(ClassRoom, id=kwargs.get('class_id'))
        user_profile= get_object_or_404(UserProfile, id=kwargs.get('user_id'))
        class_room.admin.add(user_profile)
        class_room.student.remove(user_profile)
        class_room = ClassRoomRetrieveSerializer(instance=class_room)
        return Response(class_room.data, status=200)


class RetrieveUser(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_pk'
