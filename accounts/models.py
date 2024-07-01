from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('メールアドレスを入力してください')
        if not username:
            raise ValueError('ユーザー名を入力してください')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, default='email@example.com')
    username = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email' # 一意の識別子
    REQUIRED_FIELDS = ['username'] # superuser作成に必要な項目
    
    def __str__(self):
        return self.email