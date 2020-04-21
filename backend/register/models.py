from django.db import models

# Create your models here.

# class User(models.Model):
#
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=128,unique=True)
#     password = models.CharField(max_length=256)
#     email = models.EmailField(unique=True)
#     c_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ['c_time']
#         verbose_name = 'user'
#         verbose_name_plural = 'user'

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'