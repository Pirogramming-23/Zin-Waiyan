from django.shortcuts import render,redirect,get_object_or_404
from .models import Idea, IdeaStar
from django.core.paginator import Paginator
from .forms import IdeaForm


# Create your views here.
def main(request):
    ideas = Idea.objects.all().order_by('-created_at')
    sort = request.GET.get('sort')
    if sort == 'popularity':
        ideas = ideas.order_by('-interest')
    elif sort == 'created':
        ideas = ideas.order_by('created_at')
    elif sort == 'latest':
        ideas = ideas.order_by('-created_at')
    elif sort == 'name':
        ideas = ideas.order_by('title')
    paginator = Paginator(ideas,4) # show 4 ideas per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if not request.session.session_key:
        request.session.save()

    session_key = request.session.session_key
    starred_ids = IdeaStar.objects.filter(session_key=session_key).values_list('idea_id', flat=True)
    context = {
        'ideas':ideas,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'starred_ids': starred_ids,
    }
    return render(request,'ideas/list.html',context=context)


def toggle_star(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, id=pk)

        # Use session key instead of user
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key

        star, created = IdeaStar.objects.get_or_create(idea=idea, session_key=session_key)

        if not created:
            star.delete()

    return redirect('ideas:main')  


def adjust_interest(request, pk):
    if request.method == "POST":
        idea = get_object_or_404(Idea, id=pk)
        direction = request.POST.get("direction")

        if direction == "up":
            idea.interest += 1
        elif direction == "down":
            idea.interest = max(0, idea.interest - 1)

        idea.save()
    return redirect('ideas:main')  


def create(request):
    if request.method == "GET":
        form = IdeaForm()
        context = {
            'form':form
        }
        return render(request,'ideas/create.html',context)
    else:
        form = IdeaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

def detail(request, pk):
    idea = Idea.objects.get(id=pk)

    # Get session key
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    # Check if this idea is starred
    is_starred = IdeaStar.objects.filter(
        idea=idea,
        session_key=session_key
    ).exists()

    context = {
        'idea': idea,
        'is_starred': is_starred,
        'tool': idea.devtool,
    }
    return render(request, 'ideas/detail.html', context=context)

def update(request,pk):
    idea = Idea.objects.get(id=pk) 
    if request.method == 'GET':
        form = IdeaForm(instance=idea) 
        context = {
            'form': form, 
            'idea':idea, 
        }
        return render(request, 'ideas/update.html', context=context)
    else:
        form = IdeaForm(request.POST, request.FILES, instance=idea) 
        if form.is_valid():
            form.save()
        return redirect('ideas:detail',pk=pk) 

def delete(request,pk):
    idea = Idea.objects.get(id=pk)
    idea.delete()
    return redirect('/')