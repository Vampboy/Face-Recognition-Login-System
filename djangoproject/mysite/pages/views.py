from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm,Registrationform
from django.contrib.auth import authenticate, login
import os

from django.urls import path, include

import face_recognition
import cv2 

def facedect(loc):
        cam = cv2.VideoCapture(0)   
        s, img = cam.read()
        if s:   
                
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                MEDIA_ROOT =os.path.join(BASE_DIR,'pages')

                loc=(str(MEDIA_ROOT)+loc)
                face_1_image = face_recognition.load_image_file(loc)
                face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

                #

                small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)
                

                print(check)
                if check[0]:
                        return True

                else :
                        return False    

def about(request):
    return render(request,"about.html",{})

def base(request):
        if request.method =="POST":
                form =LoginForm(request.POST)
                if form.is_valid():
                        username=request.POST['email']
                        password=request.POST['password']
                        user = authenticate(request,username=username,password=password)
                        if user is not None:
                                if facedect(user.userprofile.head_shot.url):
                                        login(request,user)
                                return redirect('index')
                        else:
                                return redirect('index')        
        else:
                MyLoginForm = LoginForm()
                return render(request,"base.html",{"MyLoginForm": MyLoginForm})  

def home(request):
   return render(request, 'home.html', {})

#from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request,"index.html",{})


def register(request):
        if request.method =="POST":
                form =Registrationform(request.POST)
                if form.is_valid():
                        form.save()
                        username=form.cleaned_data['username']
                        password=form.cleaned_data['password1']
                        user = authenticate(username=username,password=password)
                        login(request,user)
                        return redirect('index')
                else:
                        return redirect('index')        

        form =Registrationform()
        return render(request,'registration/register.html',{'form':form})        

def profile(request):
        return render(request,'profile.html',{})


def common(request):
        return render(request,'common.html',{})