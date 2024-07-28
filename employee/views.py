from django.shortcuts import redirect, render
from .models import Employee
# Create your views here.
def addshow(request):
    if request.method == "POST":
        name = request.POST['fname']
        gender = request.POST['gender']
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = Employee(Name = name, Gender = gender,Email = email, Password = pwd)
        user.save()
    data = Employee.objects.all()
    return render(request,'addshow.html',{'data':data})


def update(request,id):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":  
        emp.Name = request.POST['fname']
        emp.Gender = request.POST['gender']
        emp.Email = request.POST['email']
        emp.Password = request.POST['pwd']
        emp.save()
        return redirect('addshow')
    return render(request,'update.html',{'emp':emp})

def delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return render(request,'addshow.html')