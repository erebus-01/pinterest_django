from contextlib import nullcontext
from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField(primary_key=True)
  firstName = models.CharField(blank=True, max_length=50, null=True)
  lastName = models.CharField(max_length=50, blank=True)
  story = models.TextField(blank=True)
  profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
  website = models.CharField(max_length=20, blank=True)

  def __str__(self):
    return self.user.username
