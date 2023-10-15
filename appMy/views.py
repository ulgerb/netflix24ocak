from django.shortcuts import render, redirect
from appUser.models import Profile
from django.contrib import messages


def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

def profileLogin(request, pid):
   
   if Profile.objects.filter(user=request.user, id=pid).exists():
      # kullanıcın tüm profillerinin plogin değerini false yapar
      Profile.objects.filter(user=request.user).update(plogin=False)
      profile = Profile.objects.filter(user=request.user).get(id=pid)
      profile.plogin = True
      profile.save()
      return redirect('indexBrowsePage')
   else:
      messages.error(request, "Hatalı url yönlendirmesi")
      return redirect("loginUser")

def indexBrowsePage(request):
   # get hata verir önlem al, her kullanıcının kendi profillerine giriş yapabilmeli
   profile = Profile.objects.filter(user=request.user).get(plogin=True)
   
   
   context = {
      "profile":profile,
   }
   return render(request, 'indexbrowse.html',context)


