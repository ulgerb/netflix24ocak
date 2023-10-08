from django.shortcuts import render

# Create your views here.

def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

def indexBrowsePage(request):
   context = {}
   return render(request, 'indexbrowse.html',context)


