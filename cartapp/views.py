from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def addcategory(request):
    return render(request, 'Addcategory.html')

def category(request):
    return render(request,"category.html")