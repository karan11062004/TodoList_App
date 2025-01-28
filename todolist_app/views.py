from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from  django.contrib.auth.decorators import login_required
@login_required
def todolist(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
            messages.success(request,('New Task Added Successfully!!'))
        return redirect('todolist')
    else: 
        all_tasks=TaskList.objects.filter(manage=request.user).order_by('id')
        paginator=Paginator(all_tasks,6)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request,'todolist.html',{'all_tasks': all_tasks})
def edit_task(request,task_id):
    if request.method=='POST':
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,('Task Updated Successfully!!'))
        return redirect('todolist')
    else: 
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
def index(request):
    return render(request,'index.html',{})
def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.delete()
        messages.success(request,('Task Deleted Successfully !!'))
    else :
        messages.error(request,('Invalid User to make changes'))
    return redirect('todolist')
def done_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=True
        task.save()
    else :
        messages.error(request,('Invalid User to make changes'))
    return redirect('todolist')
def undone_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,('Invalid User to make changes'))  
    return redirect('todolist')

def about_us(request):
    return render(request,'about_us.html',{'welcome':'welcome to about us'})
def contact_us(request):
    return render(request,'contact_us.html',{'welcome':'welcome to contact us'})
