from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')