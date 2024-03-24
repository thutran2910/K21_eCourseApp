from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.decorators import action
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny]
        return [permissions.IsAuthenticated()]
    # Tao 5 cai API
    # list (GET)--> xem ds cac khoa hoc
    # list (POST)--> them khoa hoc
    # detail--> xem chi tiet 1 khoa hoc
    # put--> cap nhat
    # delete--> xoa 1 khoa hoc

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    @action(methods=['post'], detail=True, url_path="hide-lesson")
        #/lesson/{pk}/hide-lesson
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=LessonSerializer(l).data,status=status.HTTP_200_OK)

def index(request):
    return HttpResponse("Hello  e-Course App")


# Create your views here.

def welcome(request, year):
    return HttpResponse("HELLO " + str(year))


class TestView(View):
    def get(self, request):
        return HttpResponse("TESTING")

    def post(self, request):
        pass
