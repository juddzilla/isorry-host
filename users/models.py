from django.contrib.auth.models import AbstractBaseUser, UserManager

class User(AbstractBaseUser):
    objects =  UserManager()

    def __str__(self):
        return self.username