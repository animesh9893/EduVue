from django.shortcuts import render , redirect

# Create your views here.
def home(request):
    home_context={'carousel_text':['Demo1','Demo2','Demo3']}
    return render(request,'home/home.html',home_context)