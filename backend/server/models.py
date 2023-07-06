from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


class Tag(models.Model):
    tags = models.TextField(default='')

    def __str__(self):
        return self.tags


class TagLabels(models.Model):
    labels = models.TextField(default='')

    def __str__(self):
        return self.labels


class UserTagPreference(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tag_labels = models.ForeignKey(TagLabels, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.tag_labels}'
