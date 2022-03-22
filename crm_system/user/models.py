from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email address.")
        if not name:
            raise ValueError("User must have a name.")
        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_client = False
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=30, unique=True)
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_client = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','is_superuser']

    objects = AccountManager()

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
      