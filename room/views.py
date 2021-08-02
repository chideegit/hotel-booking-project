from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import RoomModel, GuestModel, GuestModelHistory
from .form import BookRoomForm

def Dashboard(request):
    obj = RoomModel.objects.all().count()
    obj1 = GuestModel.objects.all().count()
    obj2 = GuestModelHistory.objects.all().count()
    obj3 = RoomModel.objects.filter(is_booked=False).count()
    context = {'obj':obj, 'obj1':obj1, 'obj2':obj2, 'obj3':obj3}
    return render(request, 'room/dashboard.html', context)

@login_required
def BookRoomView(request):
    if request.method == 'POST':
        form = BookRoomForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            obj = RoomModel.objects.get(room_name=str(var.room))
            obj.is_booked = True
            obj.save()
            var.save()
            return redirect('dashboard')
    else:
        form =  BookRoomForm()
    context = {'form':form}
    return render(request, 'room/book_room.html', context)


@login_required
def AllGuestsView(request):
    obj = GuestModel.objects.all
    context = {'obj':obj}
    return render(request, 'room/all_guests.html', context)


@login_required
def CheckOutView(request, pk):
    obj = GuestModel.objects.get(id=pk)
    GuestModelHistory.objects.create(
        guest_name = obj.guest_name,
        room = str(obj.room),
        payment = obj.payment,
        date_booked = obj.date_booked
    )
    var = RoomModel.objects.get(room_name=str(obj.room))
    var.is_booked = False
    var.save()
    obj.delete()
    return redirect('dashboard')


@login_required
def GuestHistoryView(request):
    obj = GuestModelHistory.objects.all()
    context = {'obj':obj}
    return render(request, 'room/guest_history.html', context)