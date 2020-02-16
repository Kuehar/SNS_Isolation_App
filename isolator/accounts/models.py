from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.

class SuperUser(BaseUserManager):
    def create_user(self,email,birth_date,password=None):
        if not email:
            raise ValueError('Users must have an E-mail address')

        user = self.model(email=self.normalize_email(email),birth_date=birth_date,)


        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,birth_date,password):
        user = self.create_user(email,birth_date=birth_date,password=password)
        user.is_admin = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

