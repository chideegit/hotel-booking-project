from typing import Sequence
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import check_for_language

class RoomModel(models.Model):
    room_type = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Executive', 'Executive')
    )
    room_name = models.CharField(max_length=100)
    room_category = models.CharField(choices=room_type, max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.room_name


class GuestModel(models.Model):
    guest_name = models.CharField(max_length=100)
    room = models.OneToOneField(RoomModel, on_delete=models.CASCADE)
    payment = models.PositiveIntegerField(default=0)
    date_booked = models.DateTimeField(auto_now_add=True)


class GuestModelHistory(models.Model):
    guest_name = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    payment = models.PositiveIntegerField(default=0)
    date_booked = models.DateTimeField()
    check_out_time = models.DateTimeField(auto_now_add=True)

    


    
    