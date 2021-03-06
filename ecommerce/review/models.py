from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=256)
    updated_on = models.DateTimeField(auto_now=True)
