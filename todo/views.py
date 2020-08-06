from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from todo.models import Todo
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request,'main/index.html',{'todo_items':todo_items})
def add_todo(request):
    time=timezone.now()
    content=request.POST['content']
    Todo.objects.create(added_date=time,text=content)
    return HttpResponseRedirect('/')
