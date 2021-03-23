from django.shortcuts import render

# Create your views here.
def staff_management(request,username):
	context={}
	print(username)
	return render(request,'staffm/staffm.html',context)