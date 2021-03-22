from django.contrib import admin

# Register your models here.
from .models import WhyEduVueText
from .models import CarouselText

admin.site.register(WhyEduVueText)
admin.site.register(CarouselText)