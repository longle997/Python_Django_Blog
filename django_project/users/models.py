from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here. Create model mean create stuff we wanna store in database
# We extern User model with Profile model, which is contain image for user
class Profile(models.Model):
	# create 1 to 1 relationship with exist model, User
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# if we create a profile for an user without image, it will use default.jpg
	# when we upload image to our page, that image will be saved in profile_pics folder
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# this function will replace name of object when we interact with that object in database
	# for example, when we interact with Profile object, it only show <QuerySet [<Profile:>,<Profile:>,<Profile:>....]
	def __str__(self):
		return f'{self.user.username} Profile'

	# override the save method of class Profile
	def save(self):
		# execute the parent's class save method
		super().save()

		# take image's path
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			# make a thumbnail (small size of image) from original image
			img.thumbnail(output_size)
			# overide the old image by new resize image according to image's path
			img.save(self.image.path)