from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
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
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

        
# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def _create_user(self, email, password, **extra_fields):        
#         """
#         Create and save a User with the given email and password.
#         """
#         now = timezone.now()
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, password=password,  last_login=now, date_joined=now, **extra_fields)
#         # user.set_password(make_password(password))
#         user.save()

#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         extra_fields.setdefault('is_active', False)        
#         return self._create_user(email, password, **extra_fields)        

    # def create_superuser(self, email, password, **extra_fields):
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)

    #     # if extra_fields.get('is_staff') is not True:
    #     #     raise ValueError(_('Superuser must have is_staff=True.'))
    #     # if extra_fields.get('is_superuser') is not True:
    #     #     raise ValueError(_('Superuser must have is_superuser=True.'))
    #     # print(extra_fields.get('is_active'))
    #     # return self._create_user(email=email, password=password, is_staff=True, is_superuser=True, **extra_fields)
    #     now = timezone.now()
    #     if not email:
    #         raise ValueError(_('The Email must be set'))
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, is_staff=True, is_active=True, is_superuser=True, last_login=now, date_joined=now)
    #     user.set_password(make_password(password))
    #     user.save()
    #     return user        

    # def create_superuser(self, email, password, **extra_fields):
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError(_('Superuser must have is_staff=True.'))
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(_('Superuser must have is_superuser=True.'))
    #     return self._create_user(email, password, **extra_fields)    

    # def create_superuser(self, email, password):
    #     new = self.create_user(
    #         email,
    #         password=password
    #     )
    #     new.is_active = True
    #     new.is_staff = True
    #     new.is_superuser = True
    #     new.save(using=self._db)
    #     return new    

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email