from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    birthday_year = models.PositiveIntegerField(blank=True, default=1991)
    position = models.CharField(max_length=64, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# psycopg2-binary
