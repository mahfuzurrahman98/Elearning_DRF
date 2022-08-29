from functools import partial

from django.shortcuts import render
from numpy import empty
from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from student.serializer import StudentSerializer


class CRUD(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            if Student.objects.filter(id=id).exists() == False:
                return Response({'status': 404, 'message': 'Not found'})

            student = Student.objects.get(id=id)
            print(student)
            serializer = StudentSerializer(student)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
        return Response({'status': 200, 'data': serializer.data})

        # Create your views here.

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'message': 'Student created successfully'})
        else:
            return Response(serializer.errors)

    def put(self, request, id=None, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Student updated successfully'})
        else:
            return Response(serializer.errors)

    def delete(self, request, id=None, format=None):
        student = Student.objects.get(id=id)
        if student.delete():
            return Response({'status': 200, 'message': 'Student deleted successfully'})
        else:
            return Response({'status': 500, 'message': 'Error'})
