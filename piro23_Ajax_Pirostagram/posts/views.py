from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth import login
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST


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

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at') #newest_first

    # indicate whether logged-in user has liked the post
    for post in posts:
        post.has_liked = post.likes.filter(user=request.user).exists()
    context = {
        'posts':posts
    }
    return render(request,'posts/post_list.html',context)

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    return render(request,'posts/create_post.html',{'form':form})

@login_required
def delete_post(request,pk):
    post = get_object_or_404(Post,id=pk)
    # can only delete own post
    if post.user != request.user:
        return redirect('posts:post_list')
    if request.method == "POST":
        post.delete()
        return redirect('posts:post_list')
    return render(request, 'posts/confirm_delete.html', {'post': post})

@csrf_exempt
@login_required
def like_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)  
        post_id = data.get('id')
        post = get_object_or_404(Post, pk=post_id)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({
            'id': post.id,
            'type': 'like',
            'like_count': post.likes.count(),
            'liked': liked
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

# @csrf_exempt
# @login_required
# def add_comment_ajax(request, pk):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  # ✅ load JSON
#             content = data.get('content', '').strip()
#             if not content:
#                 return JsonResponse({'error': 'Empty content'}, status=400)

#             post = get_object_or_404(Post, pk=pk)
#             comment = Comment.objects.create(
#                 user=request.user,
#                 post=post,
#                 content=content
#             )

#             return JsonResponse({
#                 'username': request.user.username,
#                 'content': comment.content
#             })
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
@login_required
@require_POST
def add_comment_ajax(request, pk):
    post = get_object_or_404(Post, pk=pk)
    content = json.loads(request.body).get('content')
    comment = Comment.objects.create(user=request.user, post=post, content=content)
    return JsonResponse({
        'id': comment.id,  # <-- ✅ this is critical!
        'username': comment.user.username,
        'content': comment.content
    })

@csrf_exempt
@login_required
@require_POST
def delete_comment_ajax(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    response_data = {
        'id': comment.id,
        'username': comment.user.username,
        'content': comment.content
    }
    comment.delete()
    return JsonResponse({'deleted': True, **response_data})



def search_post(request):
    pass


