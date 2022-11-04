from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=30, verbose_name="Name", help_text="Name for Application")
    article = models.IntegerField(verbose_name="Article", help_text="Article for Application")
    file = models.FileField(upload_to="appfiles")
    size = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(24.0)], verbose_name="Size",
                             help_text="Detected automatically")
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Role", help_text="Select is Role")


class Role(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name="Priority",
                                   help_text="Priority integer from 1 to 10")
    def __str__(self):
        return self.title