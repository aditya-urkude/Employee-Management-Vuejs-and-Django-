from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department,Employee
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage



@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)


@csrf_exempt
def employeeApi(request,employee_identifier=None):
    if request.method=='GET':
        employees = Employee.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        print("employee_data ",employee_data)
        employee=Employee.objects.get(email = employee_data['email'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        print("employee_identifier ",employee_identifier)
        try:
            employee = Employee.objects.filter(mobile=employee_identifier)
            print("emp ",employee)
        except Employee.DoesNotExist:
            return JsonResponse({"error": f"Employee with id={employee_identifier} does not exist"}, status=404)

        if len(employee)>1:
            employee[0].delete()
        else:

            employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
        
