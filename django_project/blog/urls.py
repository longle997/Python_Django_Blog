from django.urls import path
from . import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView,
	UserPostListView
)

urlpatterns = [
    # path('', views.home, name='blog-home'),
    # when we use class view, we need to convert class into actual view by as_view() method
    # by defaul program will looking in <app>/<model>_<view type>.html
    # for example: blog/post_list.html
    path('', PostListView.as_view(), name='blog-home'),
    # localhost:8000/user/longhuynh will match this pattern and Django will call
    # the function UserPostListView(username = 'longhuynh')
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # pk is primary key, pk is automatically add to a row when it was created
    # because detail view is working with Post model, and post object has pk
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # post update is using same template with post detail
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # post-delete will use post_confirm_delete.html template
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
