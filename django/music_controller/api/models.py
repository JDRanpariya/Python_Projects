from django.db import models
import random
import string

# Create your models here.

def generate_unique_code():
    len = 6

    while True:
         code = ''.join(random.choices(string.ascii_uppercase, k=len))
         if Room.objects.filter(code=code).count() == 0:
             break
    return code


class Room(models.Model):
    code = models.CharField(max_length=50, default=" ", unique=True)
    host = models.CharField(max_length=50, default=" ", unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    created_at = models.DateField(auto_now_add=True)
    votes_to_skip = models.IntegerField(null=False, default=1)

