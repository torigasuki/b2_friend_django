from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    phoneNumberRegex = RegexValidator(
        regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(
        validators=[phoneNumberRegex], max_length=11, null=True, default='')
    address = models.CharField(max_length=3, default='')
    bio = models.CharField(max_length=256, default='')

