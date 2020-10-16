from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    """def get_absolute_url(self):
        username = User.get_username
        return reverse('user:author_info', args=[self.username])"""
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)

class Profile(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    avatar = models.ImageField(upload_to='profile/%y/%m/%d', null=True, blank=True)
    bio = models.TextField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    fa_account = models.URLField(null=True, blank=True)
    tw_account = models.URLField(null=True, blank=True)
    in_account = models.URLField(null=True, blank=True)
    li_account = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.owner.username

    def get_absolute_url(self):
        return reverse('user:profile', args=[self.owner.id])        