from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import students
from .serializers import StudentSerializers



class StudentsView(APIView):

    def get_student(self, pk):
        try:
            student = students.objects.get(studentId=pk)
            return student
        except students.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializers(data)
        else:
            data = students.objects.all()
            serializer = StudentSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("students Added Successfully", safe=False)
        return JsonResponse("Failed to Add students", safe=False)

    def put(self, request, pk=None):
        student_to_update = students.objects.get(studentId=pk)
        serializer = StudentSerializers(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("students updated Successfully", safe=False)
        return JsonResponse("Failed To Update students")

    def delete(self, request, pk):
        student_to_delete = students.objects.get(studentId=pk)
        student_to_delete.delete()
        return JsonResponse("students Deleted Successfully", safe=False)