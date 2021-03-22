from django.shortcuts import render , redirect
from .models import WhyEduVueText , CarouselText

def get_wevt_model_data(obj):
    l=[]
    l.append(obj.head_text)
    l.append(obj.abbrivationtext)
    return l
    
def get_carousel_model_data(obj):
    return obj.head_text

# Create your views here.
def home(request):
    wevt=list(map(get_wevt_model_data,WhyEduVueText.objects.filter(display=True)))
    carousel_text=map(get_carousel_model_data,CarouselText.objects.filter(display=True))
    # print(carousel_text)
    home_context={
    	'carousel_text':carousel_text,
    	'why_eduvue_text':wevt,
    }
    return render(request,'home/home.html',home_context)





