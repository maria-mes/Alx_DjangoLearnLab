from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followed_by',  # changed from 'followers'
        blank=True
    )
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
