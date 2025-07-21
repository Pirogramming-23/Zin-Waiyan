from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Go to login after signup
    else:
        form = UserCreationForm()
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


