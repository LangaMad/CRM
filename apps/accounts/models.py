from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)



class Manager(AbstractUser):
    username = None
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Эл.почта', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    number_of_deals = models.PositiveIntegerField(default=0, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'




