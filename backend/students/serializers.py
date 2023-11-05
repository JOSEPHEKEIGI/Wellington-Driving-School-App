from rest_framework import serializers
from .models import students

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=students
        fields= ('studentsId',
                 'FirstName',
                 'LastName',
                 'RegistrationNo',
                 'Email',
                 'Course')