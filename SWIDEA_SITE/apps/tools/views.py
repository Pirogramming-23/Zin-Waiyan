from django.shortcuts import render,redirect
from .models import Tool
from .forms import ToolForm

# Create your views here.
def tools_list(request):
    tools = Tool.objects.all()
    context = {
        'tools':tools,
    }
    return render(request,'tools/tools_list.html',context)

def create(request):
    if request.method == 'GET':
        form = ToolForm()
        context = {
            'form':form,
        }
        return render(request,'tools/create.html',context)
    else:
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save()
        return redirect('tools:detail',pk=tool.pk)

def detail(request,pk):
    tool = Tool.objects.get(id=pk)
    context = {
        'tool':tool,
    }
    return render(request,'tools/detail.html',context)

def update(request,pk):
    tool = Tool.objects.get(id=pk)
    if request.method == 'GET':
        form = ToolForm(instance=tool)
        context = {
            'form':form,
            'tool': tool,
        }
        return render(request,'tools/update.html',context)
    else:
        form = ToolForm(request.POST,instance=tool)
        if form.is_valid():
            form.save()
        return redirect('tools:detail',pk=tool.pk)

def delete(request,pk):
    tool = Tool.objects.get(id=pk)
    tool.delete()
    return redirect('tools:tools_list')