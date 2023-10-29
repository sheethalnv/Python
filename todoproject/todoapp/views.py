
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from todoapp.forms import Todoform
from todoapp.models import Task


# Create your views here.
class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'


class Taskupdateview(UpdateView):
    model=Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')


def home(request):
    task1=Task.objects.all()
    if request.method=="POST":

        name =request.POST.get('tname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()


    return render(request,"home.html",{'task1':task1})

def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None,request.FILES,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})
