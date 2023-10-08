from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# PROJE
# netflix sayfasında video kartları eklenicek (resim)
# videolar arasında kategori oluşturulucak.
# listem kısmını yapana 30 puan (proje yada final)
# 19.10.23 son teslim deadline


def profileUser(request):
   
   profile_list = Profile.objects.filter(user=request.user)

   if request.method =="POST":
      submit = request.POST.get("submit")

      if submit == "padd":
         title=  request.POST.get("title")
         image= request.FILES.get("image")
         kid= request.POST.get("kid")

         if not kid:
            kid = False
         
         p = Profile(user=request.user,title=title, image=image, kid=kid)
         p.save()
         
         return redirect('profileUser')
      
   
   context = {
       'profile_list': profile_list,
   }
   return render(request, 'user/profile.html',context)

def accountUser(request):
   context = {}
   return render(request, 'user/account.html',context)

def loginUser(request):

   if request.method == "POST":
      username = request.POST.get("username") # basriberkay@gmail.com, okan@gmail.com
      password = request.POST.get("password")

      if User.objects.filter(email=username).exists():
         username = User.objects.get(email=username).username
      
      user = authenticate(username=username, password=password)

      if user is not None:
         login(request, user)
         messages.success(request, "Giriş Yaptınız..")

         return redirect("profileUser")
      else:
         messages.error(request, "Kullanıcı adı veya şifre yanlış!!")
      
   
   context = {}
   return render(request, 'user/login.html',context)

def registerUser(request):

   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")

      bool_p = bool_u = bool_e = True
      if password1 != password2:
         messages.error(request, "Şifreler aynı değil")
         bool_p = False
      
      if User.objects.filter(username=username).exists():
         messages.error(request, "Kullanıcı adı zaten var")
         bool_u = False
      
      if User.objects.filter(email=email).exists():
         messages.error(request, "Email zaten kullanılıyor")
         bool_e = False
         
      if bool_p and bool_u and bool_e:
         user = User.objects.create_user( username=username, email=email, password=password1 ,first_name=fname, last_name=lname)
         user.save()
         return redirect("loginUser")
      
      # if password1 == password2:
      #    if not User.objects.filter(username=username).exists():
      #       if not User.objects.filter(email=email).exists():
      #          user = User( username=username, email=email, password=password1 ,first_name=fname, last_name=lname)
      #          user.save()
      #       else:
      #          messages.error(request, "email zaten var")
      #    else:
      #       messages.error(request, "Kullanıcı zaten var")
      # else:
      #    messages.error(request, "şifreler aynı değil")
         
   context = {}
   return render(request, 'user/register.html',context)