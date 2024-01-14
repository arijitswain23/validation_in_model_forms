from django.shortcuts import render

from app.forms import *

from django.http import HttpResponse

# Create your views here.
def create_school(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('Create School Successful')
        else:
            return HttpResponse('Invalid Data')
        
    return render(request,'create_school.html',d)