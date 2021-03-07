from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccount(models.Model):

    COUNTY_CHOICES = (
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UA', 'Ukraine')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    pic = models.ImageField(upload_to='account', default='account/default.png')
    full_address = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=32)
    country = models.CharField(choices=COUNTY_CHOICES, max_length=2)
    telephone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name
