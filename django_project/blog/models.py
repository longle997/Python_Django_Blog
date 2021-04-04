from django.db import models
from django.utils import timezone
# User is a default model in database that store information about user that we have created
from django.contrib.auth.models import User
from django.urls import reverse

# model is what we store in database
# post model store information about post inside a table in database
# Post model is inherit property from Model model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Error No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
	# this error was cause because after create new form, CreateView don't know where to redirect
	# That's why we need to define the absolute url for this model, because CreateView is working with this model
    def get_absolute_url(self):
    	# by provide absolute url, CreateView know where to point after successfully submit
        return reverse('post-detail', kwargs={'pk': self.pk })