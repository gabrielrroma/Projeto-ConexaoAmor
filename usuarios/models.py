from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("O nome de usuário é obrigatório")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superusuários devem ter is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superusuários devem ter is_superuser=True.")

        return self.create_user(username, password=password, **extra_fields)

class Professor(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # Remova os campos obrigatórios

    def __str__(self):
        return self.username

class AdminOng(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def is_adminong(self):
        # Adicione a lógica para verificar se o usuário é um administrador da ONG
        # Por exemplo, se você quiser que todos os usuários AdminOng sejam considerados administradores,
        # você pode simplesmente retornar True
        return True

# Adicione o related_name aos campos de grupos e permissões em um dos modelos
AdminOng._meta.get_field('groups').remote_field.related_name = 'adminong_groups'
AdminOng._meta.get_field('user_permissions').remote_field.related_name = 'adminong_user_permissions'
