from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import NewCourseForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm


def home(request):
    courses = Course.objects.all()
    return render(request,'home.html',{'courses':courses} )



def course_detail(request,id):
    course = Course.objects.get(pk=id)
    return render(request,'course_detail.html',{'course':course})



def add_course(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('home')
    else:
        form = NewCourseForm()
    return render(request,'add_course.html',{'form':form})




def backend(request):
    courses = Course.objects.all()
    return render(request,'backend.html',{'courses':courses} )
    
def edit(request,id):
    course = Course.objects.get(pk=id)
    form = NewCourseForm(instance=course)
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES,instance=course)
        if form.is_valid():
            course=form.save(commit=False)
        course.save()
        
        return redirect('home')
    # else:
    #     form = NewCourseForm(request,instance=course)
    return render(request,'backend/edit.html',{'form':form, 'course': course })


def delete(request, id):
    if request.method == 'POST':
        course = Course.objects.get(pk=id)
        print(id,'To delete')
        course.delete()
        return redirect('backend')
    else:
        return render(request,'backend/delete.html')   


def login(request):
    form = UserCreationForm()

    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()  


    context = {'form':form}

    return render(request, 'login.html',context)



def signup(request):
    if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
             user = form.save()  
             auth_login(request,user)
             return redirect('login')

    else:
        form = CreateUserForm()
    return render(request,'signup.html',{'form': form})



    

# Create your views here