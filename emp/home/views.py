from django.shortcuts import render,redirect
from .models import Emp


# Create your views here.
def emp_home(request):
    emps = Emp.objects.all()
    return render(request , "index.html" , {
        'emps':emps
    })

#fetching  name 

def add_emp(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_address = request.POST.get("emp_address")
        emp_phone = request.POST.get("emp_phone")
        emp_department = request.POST.get("emp_department")
        emp_working = request.POST.get("emp_working")

        e = Emp(
            name=emp_name,
            id=emp_id,
            address=emp_address,
            phone=emp_phone,
            department=emp_department,
            working=bool(emp_working) if emp_working is not None else False
        )

        # saving
        e.save()

        return redirect("/home/")

    return render(request, "add_emp.html", {})


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/home/")


def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request , 'update_emp.html' , {
        'emp':emp
    })
    
def do_update_emp(request, emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_address = request.POST.get("emp_address")
        emp_phone = request.POST.get("emp_phone")
        emp_department = request.POST.get("emp_department")
        emp_working = request.POST.get("emp_working")

        # Retrieve the existing employee instance from the database
        emp = Emp.objects.get(pk=emp_id)

        # Update the attributes of the existing employee
        emp.name = emp_name
        emp.id = emp_id_temp
        emp.address = emp_address
        emp.phone = emp_phone
        emp.department = emp_department
        emp.working = bool(emp_working) if emp_working is not None else False

        # Save the updated employee
        emp.save()

        return redirect("/home/")

    return render(request, "update_emp.html", {})

