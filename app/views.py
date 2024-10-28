from django.shortcuts import render, redirect
from .models import Subject, Teacher, Student, Headmaster, Class, Exam
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import HeadmasterForm

def home(request):
  return render(request, 'Home.html')

def studentDetail_view(request):
  return render(request, 'StudentDetails.html')

def subjectDetails_view(request):
  subjects = Subject.objects.all()
  context = {
    'subjects': subjects
  }
  return render(request, 'SubjectDetails.html', context)

def testDetails_view(request):
  return render(request, 'TestDetails.html')
  
def login_view(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return redirect('home')
  else:
    print('User is not existed!')
  
  return render(request, 'login.html')

def signup_view(request):
  form = HeadmasterForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('home')
  else:
    print('Error')
  return render(request, 'signup.html', {'form':form})

def logout_view(request):
  logout(request)
  return redirect('logout_view')