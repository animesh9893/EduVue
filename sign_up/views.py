from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def sign_up(request):
    context={
        'message':'',
    }
    if request.POST:
        user_name= request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        institute_name=request.POST.get('institute_name')
        # print(user_name,password,confirm_password,institute_name)
        if len(list(User.objects.filter(user_name=user_name)))!=0:
            context['message']="Use Different User Name"
            return render(request,'sign_up/sign_up.html',context)
        elif password!=confirm_password:
            context['message']="Please fill same password"
            return render(request,'sign_up/sign_up.html',context)
        else:
            u=User(user_name=user_name,password=password,active=True,institution_name=institute_name)
            u.save()
            return redirect(u,permanent=True)

    
    return render(request,'sign_up/sign_up.html',context)