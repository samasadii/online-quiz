from django.contrib import admin
from django.urls import path

from rest_framework import routers

from classapp.views import CreateUser, Authentication, CreateClassRoom, RetrieveClassRoom, RetrieveUserClassRooms, \
    JoinClassRoom, CreateExam, AddAdminToClassRoom, RetrieveClassRoomExams, TakeExam, RetrieveExamQuestions

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/', CreateUser.as_view()),
    path('user/login/', Authentication.as_view()),
    path('user/<int:user_id>/join/class-room/<slug:address>/', JoinClassRoom.as_view()),
    path('user/<int:user_id>/admin/class-room/<int:class_id>/', AddAdminToClassRoom.as_view()),

    path('class/create/', CreateClassRoom.as_view()),
    path('class/<int:class_id>/', RetrieveClassRoom.as_view()),
    path('classes/<int:user_id>/', RetrieveUserClassRooms.as_view()),

    path('take-exam/', TakeExam.as_view()),
    path('exam/create/', CreateExam.as_view()),
    path('exams/<int:class_id>/', RetrieveClassRoomExams.as_view()),
    path('exam/<int:exam_id>/questions/', RetrieveExamQuestions.as_view()),
]
