from functools import partial

from django.shortcuts import render
from numpy import empty
from rest_framework.decorators import api_view
from rest_framework.response import Response

from student.models import Student
from student.serializer import StudentSerializer


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def crud(request, id=None):
    if request.method == 'GET':
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

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'message': 'Student created successfully'})
        else:
            return Response(serializer.errors)

    if request.method == 'PUT':
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Student updated successfully'})
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        student = Student.objects.get(id=id)
        if student.delete():
            return Response({'status': 200, 'message': 'Student deleted successfully'})
        else:
            return Response({'status': 500, 'message': 'Error'})
