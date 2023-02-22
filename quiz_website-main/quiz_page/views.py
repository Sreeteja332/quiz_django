from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import Http404


from .forms import RegisterUserForm

from .models import *

import random

# Create your views here.

def starting_page(request):
    try:
        return render(request,"quiz_page/index.html")
    except:
        raise Http404()

def login_user(request):
    try:
        if request.method == 'POST':
            username = request.POST['user_id1']
            password = request.POST['pwd1']
            user = authenticate(request,username=username,password=password)
            print(username)
            print(password)
            print(user)

            if user is not None:
                login(request,user)
                return redirect("dashboard")
            else:
                messages.success(request,("Username or Password are incorrect, Try Again!"))
                return render(request,"quiz_page/login.html",{})
        else:
            return render(request,"quiz_page/login.html",{})
    except:
        raise Http404()

def logout_user(request):
    try:
        logout(request)
        messages.success(request,("Successfully Logged Out"))
        return redirect("starting_page")
    except:
        raise Http404()

def register_user(request):
    try:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username,password=password)
                login(request,user)
                messages.success(request,("Registration Successful!"))
                return redirect("dashboard")
        else:
            form = RegisterUserForm()

        return render(request,"quiz_page/register.html",{
            'form':form
        })
    except:
        raise Http404()

def student_dashboard(request):
    try:
        results = QuizResult.objects.filter(user=request.user)
        return render(request,"quiz_page/student_dashboard.html",{
            "results": results
        })
    except:
        raise Http404()

def quiz(request):
    try:
        exam = Exam.objects.all()
        exam = random.sample(list(exam),10)
        if request.method == 'POST':
            score = 0
            wrong = 0
            correct = 0
            total = 0
            for i in exam:
                total+=1
                ans = request.POST.get(i.question)
                print(ans)
                print(i.corrans)
                print()
                if i.corrans == request.POST.get(i.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            percent = score/(total*10) * 100
            result = QuizResult(user=request.user,score=score)
            result.save()
            context = {
                'score': score,
                'correct': correct,
                'wrong': wrong,
                'percent': percent,
                'total': total
            }
            return render(request,"quiz_page/result.html",context)
        else:
            return render(request,"quiz_page/quiz.html",{
            "exam": exam
            })
    except:
        raise Http404()

def result(request):
    try:
        return render(request,"quiz_page/result.html")
    except:
        raise Http404()