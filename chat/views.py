from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse
from .forms import SignupForm
from .models import Room, Message

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup') 
    else:
        form = SignupForm()
    return render(request, 'chat/signup.html', {'form': form})

@login_required 
def room_detail(request, slug):
    # On utilise la version de Becker (get_object_or_404) car elle est plus sûre
    room = get_object_or_404(Room, slug=slug)
    messages = room.messages.all()
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'messages': messages
    })

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        room_id = request.POST.get('room_id')
        
        if content and room_id:
            room = get_object_or_404(Room, id=room_id)
            new_message = Message.objects.create(
                room=room,
                user=request.user,
                content=content
            )
            return JsonResponse({
                'status': 'success',
                'message_id': new_message.id,
                'user': new_message.user.username,
                'content': new_message.content,
                'timestamp': new_message.timestamp.strftime('%H:%M')
            })
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def flag_message(request, message_id):
    # La nouvelle fonctionnalité de Becker
    if request.method == 'POST':
        message = get_object_or_404(Message, id=message_id)
        message.is_flagged = True 
        message.save()
        return redirect('room_detail', slug=message.room.slug)
    return redirect('signup')