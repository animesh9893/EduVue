from django.shortcuts import render
from .models import Staff
from sign_up.models import User

context={
	'add_staff':False,
	'delete_staff':False,
}
# Create your views here.
def staff_management(request,username):
	s=list(Staff.objects.all())
	print(username)
	context['url']="/staff_management/"+username+"/"
	context['number_of_staff']=len(s)
	u=User.objects.get(user_name=username)
	context['user_name']=u
	print(context['user_name'])
	context['institution_name']=u.institution_name
	print(context['institution_name'])

	if request.POST:
		name=request.POST.get('name')
		subject=request.POST.get('subject')
		password=request.POST.get('password')
		salary=request.POST.get('salary')
		user_obj = User.objects.get(user_name=username)
		u=Staff(name=name,subject=subject,password=password,salary=salary,attendance=0,admin=user_obj)
		u.save()

	return render(request,'staffm/staffm.html',context)

