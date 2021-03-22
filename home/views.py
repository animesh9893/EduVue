from django.shortcuts import render , redirect

# Create your views here.
def home(request):
    home_context={
    	'carousel_text':['Demo1','Demo2','Demo3'],
    	'why_eduvue_text':[
    	['Cost','This will cost you less than $9/mo'],
    	['Support','Support team works all 365 days. We will solve your problem within 24 hours.'],
    	['Website','Free Website with domain name.'],
    	['Learning Management System (LMS)','We provide LMS for students for perform all task asign by institution.'],
    	['Staff and Student Attandance Management','We use latest technology for attandance.'],
    	['Invoice & Expense Tracking and Management','Automated payment reminders to students, Staff salary disbursal system, Current P&L statement for month year, Expense tracking'],
    	['Online assessment tool','Plateform for online exam'],
    	[' Question Bank Management System','Practice Question for students'],
    	['Mock Test Platform for students','To practise for various exams'],
    	['Analytic Reporting System','provide student report.'],
    	['Mobile Application','To access course from anywhere'],
    	]
    }
    return render(request,'home/home.html',home_context)





