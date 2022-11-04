from django.contrib.auth.models import User
from django.db import models
from django.core.validators import *


class Profile(models.Model):

    validate_errors = {
        'cull_number':"Номер не должен превышать длину в 12 символов",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    call_number = models.CharField(max_length=12,  verbose_name="Номер телефона", help_text="Введите номер телефона",
                                   validators=[MaxLengthValidator(12,
                                                                  message="Номер не должен превышать длину в 12 символов"),MinLengthValidator(1, message="d")])
    token_code = models.CharField(max_length=255, verbose_name="Ваш токен", help_text="Генерируется автоматически")
    age = models.IntegerField(validators=[MinValueValidator(18 , message="Число не должно быть меньше 18"), MaxValueValidator(60, message="Число не должно превышать 60")],
                              verbose_name="Возраст",
                              help_text="Введите возраст (18-60)")

    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

    def __str__(self):

        return self.user.__str__()


class Role(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название роли")
    priority = models.IntegerField(choices=(('C', 1), ('B', 2), ('I', 3)))

    def __str__(self):
        return self.title
