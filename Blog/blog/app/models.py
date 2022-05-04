from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,UserManager,BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()
# Create your models here.
"""
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, profile_picture, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)  # change password to hash
        user.profile_picture = profile_picture
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user
"""

class usuario(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'Nombre: {self.username} - Contrasena: {self.password1} - E-Mail: {self.email}'

class post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'


