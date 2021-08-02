from django import forms

from .models import RoomModel, GuestModel

class BookRoomForm(forms.ModelForm):
    class Meta:
        model =  GuestModel
        fields = ['guest_name', 'room', 'payment']

