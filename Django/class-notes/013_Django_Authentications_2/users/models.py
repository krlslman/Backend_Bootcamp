from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(model.Model):
	portfolio = models.URLField(blank=True)
	profile_pic = models.ImageFields.(upload_to='profile_pics',blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)