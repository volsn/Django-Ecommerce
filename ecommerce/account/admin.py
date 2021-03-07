from django.contrib import admin
from account.models import UserAccount

# Register your models here.


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass
