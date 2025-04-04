from django.shortcuts import render,redirect
from foreignkeyapp.models import Course
from foreignkeyapp.models import Student
# Create your views here.

def home(request): 
    return render(request,'home.html') 
def addcourse(request): 
    return render(request,'addcourse.html') 
def addstudent(request): 
    courses=Course.objects.all()
    return render(request,'addstudent.html',{'course':courses}) 
def show_student(request): 
    return render(request,'show_student.html') 

def add(request): 
    if request.method == 'POST': 
        coursename=request.POST['coursename'] 
        coursefee=request.POST['coursefee'] 
        cou=Course( coursename=coursename, coursefee=coursefee) 
        cou.save() 
        return redirect('addstudent')
    
def add_student(request):
 if request.method == 'POST': 
    student_name=request.POST['name'] 
    student_address=request.POST['address'] 
    age=request.POST['age'] 
    joining_date=request.POST['joining_date'] 
    sel=request.POST['sel']
    print(sel)
    course1=Course.objects.get(id=sel)
    print(course1)
    student=Student(student_name=student_name,student_address=student_address,age=age,joining_date=joining_date,Course=course1)
    student.save()
    return redirect('show_student')
 
def show_student(request):
    student=Student.objects.all()
    return render(request,'show_student.html',{'students':student}) 




def editpage(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit.html',{'stud':student,'Course':course})

def edit_student_details(request,pk):
    if request.method == 'POST': 
         student=Student.objects.get(id=pk)  
         student.student_name=request.POST['name'] 
         student.student_address=request.POST['address'] 
         student.age=request.POST['age'] 
         student.joining_date=request.POST['joining_date'] 
         sel=request.POST['sel']
         course1=Course.objects.get(id=sel)
         student.Course=course1
         student.save()
         return redirect('show_student')
    return render(request,'edit.html')

def deletepage(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return redirect('show_student')




