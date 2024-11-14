from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", default='avatars/default-avatar.jpg', blank=True, null=True)
    

    def __str__(self):
        return self.user.username