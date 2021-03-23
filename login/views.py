from django.shortcuts import render,redirect
from sign_up.models import User

# Create your views here.
def login(request):
    context={
        'message':'',
    }
    if request.POST:
        user_name= request.POST.get('username')
        password=request.POST.get('password')
        print(user_name,password)
        if len(list(User.objects.filter(user_name=user_name,password=password)))==0:
            context['message']="Please use correct info"
            return render(request,'login/login.html',context)
        u=User.objects.get(user_name=user_name,password=password)
        return redirect(u,permanent=True)
    return render(request,'login/login.html',context)