from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# this is call class base view, which does same thing with home function
# inherit  from class ListView
class PostListView(ListView):
	model = Post
	# <app>/<model>_<view type>.html
	template_name = 'blog/home.html'
	# by this time, program doesn't which object it need to render
	# in home.html we loop through 'post' object
	# but by default, class view will look for 'object_list' object instead
	context_object_name = 'posts'
	# change order of post list from latest to oldest
	ordering = ['-date_posted']
	# 2 posts per page
	paginate_by = 5

# limit the post by user name from url
class UserPostListView(ListView):
	model = Post
	# <app>/<model>_<view type>.html
	template_name = 'blog/user_posts.html'
	# by this time, program doesn't which object it need to render
	# in home.html we loop through 'post' object
	# but by default, class view will look for 'object_list' object instead
	context_object_name = 'posts'

	paginate_by = 5

	def get_queryset(self):
		# get object of User model with username is from url
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		# return post object only with author value = current user name
		# because we will overide query that this view is making, it also overide the ordering
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

# By passing LoginRequiredMixin, we rule that user need to login before create new post
# UserPassesTestMixin used to make only author of a post can modify it
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	# Error NOT NULL constraint failed: blog_post.author_id
	# overide the form_valid method of CreateView class
	# in order to setting the author before this method was called
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	# Error NOT NULL constraint failed: blog_post.author_id
	# overide the form_valid method of CreateView class
	# in order to setting the author before this method was called
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# UserPassesTestMixin will run this function to check is author of this post modify it
	def test_func(self):
		# get the current post
		post = self.get_object()
		# self.request.user will take current login user
		# post.author will take author of curren update post
		if self.request.user == post.author:
			return True
		return False

# for delete view, we want to authenticate that only author of this post can delete it
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	# No URL to redirect to. Provide a success_url.
	success_url = '/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# UserPassesTestMixin will run this function to check is author of this post modify it
	def test_func(self):
		# get the current post
		post = self.get_object()
		# self.request.user will take current login user
		# post.author will take author of curren update post
		if self.request.user == post.author:
			return True
		return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
