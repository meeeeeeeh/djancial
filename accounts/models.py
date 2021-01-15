from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username=None, gender=None):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        print(email)
        return self.get(email=email)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICE = (
        ("Male", "Мужской"),
        ("Female", "Женский")
    )
    username = models.CharField(max_length=30, unique=True, blank=False,
                                error_messages={'unique': "Имя пользователя уже используется."})
    email = models.EmailField(unique=True, blank=False,
                              error_messages={'unique': "Пользователь с этим адресом уже зарегистрирован."})
    gender = models.CharField(max_length=7, choices=GENDER_CHOICE, blank=True)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'gender']

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __unicode__(self):
        return self.email
