from django.shortcuts import render , redirect
from .models import WhyEduVueText

def get_wevt_model_data(obj):
    l=[]
    l.append(obj.head_text)
    l.append(obj.abbrivationtext)
    return l
    

# Create your views here.
def home(request):
    wevt=list(map(get_wevt_model_data,WhyEduVueText.objects.filter(display=True)))
    print(wevt)    
    home_context={
    	'carousel_text':['Demo1','Demo2','Demo3'],
    	'why_eduvue_text':wevt,
    }
    return render(request,'home/home.html',home_context)





