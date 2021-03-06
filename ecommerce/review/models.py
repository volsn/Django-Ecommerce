from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=256)
    updated_on = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
