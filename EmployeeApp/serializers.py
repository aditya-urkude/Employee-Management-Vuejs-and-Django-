from rest_framework import serializers
from EmployeeApp.models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('dept_name','type','address_block')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('emp_name','address','mobile','email','dob','doj','gender','dept_id')