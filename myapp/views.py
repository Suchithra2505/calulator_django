from django.shortcuts import render
from .models import Emp,Course,Login,User
# Create your views here.
#on 25th oct
def employee(request):
    if request.method=='POST':
        emp_name=request.POST.get('empname')
        emp_desig = request.POST.get('empdesignation')
        emp_salary = request.POST.get('empsalary')
        emp_obj=Emp()
        emp_obj.name=emp_name
        emp_obj.designation = emp_desig
        emp_obj.salary=emp_salary
        emp_obj.save()
        return viewemployee(request)
    return render(request,"Employee.html")
def deleteemployee(request,id):
    emp = Emp.objects.get(id=id)
    emp.delete()
    return viewemployee(request)
#on 30th oct
def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        user = request.POST.get("uname")
        pwd = request.POST.get("passwd")
        course = request.POST.get("course")
        if len(request.FILES) != 0:
            pp = request.FILES['pp']
        else:
            pp = 'images/img_1.png'
        loginobj = Login()
        loginobj.username = user
        loginobj.password = pwd
        loginobj.save()

        userobj = User()
        userobj.loginid = loginobj
        userobj.name = name
        userobj.dob = dob
        userobj.email = email
        userobj.course = Course.objects.get(id=course)
        userobj.profilepic = pp
        userobj.save()
        return render(request, "login.html")
    courses=Course.objects.all()
    return render(request,"Registration.html",{'courses':courses})
#on 1nov
def login(request):
    if (request.method == 'POST'):
        user = request.POST.get('uname')
        sname = request.POST.get('uname')
        pwd = request.POST.get('passwd')
        if Login.objects.filter(username=user, password=pwd).exists():
            currentuser = Login.objects.get(username=user, password=pwd)
            request.session['userid'] = currentuser.id
            if currentuser.role == 0:
                users = User.objects.all()
                return render(request, "admin/adminhome.html", {'users': users})
            else:
                user = User.objects.get(loginid=currentuser)
                courses = Course.objects.all()
                propic = 'Uploads/' + str(user.profilepic)
                dd = user.dob
                return render(request,"profile.html",{'user':user,'courses':courses,'uname':sname,'propic':propic,'dd':dd})
        else:
            return render(request, "login.html", {'error': 'Login Failed'})
    return render(request, "login.html")
#on 27oct
def editemployee(request,id):
    if request.method=='POST':
        emp_name = request.POST.get('empname')
        emp_desig = request.POST.get('empdesignation')
        emp_salary = request.POST.get('empsalary')
        emp_obj = Emp.objects.get(id=id)

        emp_obj.name = emp_name
        emp_obj.designation = emp_desig
        emp_obj.salary = emp_salary
        emp_obj.save()
        return viewemployee(request)
    else:
        emp = Emp.objects.get(id=id)
        return render(request,"EditEmployee.html",{'emp':emp})
#on 22 oct
def viewemployee(request):
    employ=Emp.objects.all();
    return render(request,"ViewEmployee.html",{'employ':employ})
def arith(request):
    if request.method == 'POST':
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        op = request.POST.get("op")
        if op == "+":
            result = "Sum=" + str((num1 + num2))
        elif op == "-":
            result = "Difference=" + str((num1 - num2))
        elif op == "*":
            result = "Product=" + str((num1 * num2))
        elif op == "/":
            result = "Quotient=" + str((num1 // num2))
        elif op == "%":
            result = "Remainder=" + str((num1 % num2))
        return render(request, "simplarith.html", {'result': result})
    else:
        return render(request, "simplarith.html")

def index(request):
    return render(request,"index.html")