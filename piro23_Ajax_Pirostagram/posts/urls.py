from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'posts'

urlpatterns = [
    # Posts
    path('post_list/',views.post_list,name='post_list'),
    path('create_post/',views.create_post,name='create_post'),
    path('delete_post/<int:pk>/',views.delete_post,name='delete_post'),

    # Likes (using ajax)
    path('like_ajax/', views.like_ajax, name='like_ajax'),

    # Comments
    path('add_comment_ajax/<int:pk>/', views.add_comment_ajax, name='add_comment_ajax'),
    path('delete_comment_ajax/<int:pk>/', views.delete_comment_ajax, name='delete_comment_ajax'),

    # Search
    path('search_post/',views.search_post,name='search_post'),

    # signup
    path('', views.signup, name='signup'),

    # login
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # logout
    path('logout/', auth_views.LogoutView.as_view(next_page='posts:login'), name='logout'),

    # (Optional) 
    # path('search_user/', views.search_user, name='search_user'),
    # path('sort_post/', views.sort_post, name='sort_post'),
    # path('add_reply/<int:comment_id>/', views.add_reply, name='add_reply'),
]
