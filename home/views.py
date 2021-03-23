from django.shortcuts import render , redirect
from .models import WhyEduVueText , CarouselText
from sign_up.models import User

context={
    'status':False,
    'plan_active':False,#true if paid
    'user':None,
}

def get_wevt_model_data(obj):
    l=[]
    l.append(obj.head_text)
    l.append(obj.abbrivationtext)
    return l
    
def get_carousel_model_data(obj):
    return obj.head_text

# Create your views here.
def home(request):
    global context
    wevt=list(map(get_wevt_model_data,WhyEduVueText.objects.filter(display=True)))
    carousel_text=map(get_carousel_model_data,CarouselText.objects.filter(display=True))
    # print(carousel_text)
    context['status']=False
    context['carousel_text']=carousel_text
    context['why_eduvue_text']=wevt
    return render(request,'home/home.html',context)

def user_home(request,pk):
    global context
    user_obj = User.objects.get(id=pk)
    context['user_name']=user_obj.user_name
    context['user']=user_obj
    context['status']=True
    print(context['plan_active'])
    return render(request,'home/home_user.html',context)

def about_us(request):
    global context
    return render(request,'home/about_us.html',context)

def contact_us(request):
    global context
    return render(request,'home/contact_us.html',context)

def pricing(request):
    global context
    return render(request,'home/pricing.html',context)

def payment(request):
    global context
    if request.POST and context['user']!=None:
        card_number = request.POST.get('card_number')
        date = request.POST.get('date')
        cvv = request.POST.get('cvv')
        print(card_number,cvv,date)
        context['plan_active']=True
        context['user'].plan_true()
        context['user'].save()
        return redirect(context['user'])
    return render(request,'home/payment.html',context)

