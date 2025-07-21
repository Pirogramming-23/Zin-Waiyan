from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login
from .forms import CustomSignupForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post_list')
    else:
        form = CustomSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def post_list(request):
    pass 

def create_post(request):
    pass

def delete_post(request,pk):
    pass

def like_post(request,pk):
    pass

def add_comment(request,pk):
    pass

def delete_comment(request,pk):
    pass

def search_post(request):
    pass


