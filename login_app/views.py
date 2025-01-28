from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from login_app.forms import CustomForm
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method=='POST':
        reg_form=CustomForm(request.POST) 
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,("New user created successfully !!"))
            return redirect('login')
        else :
            return HttpResponse(reg_form.errors.as_json())


        
    else:
        register_form=CustomForm()
        return render(request,'register.html',{'register_form':register_form})
