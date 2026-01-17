from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.http import JsonResponse
from .models import Room, Message
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup') # À modifier plus tard vers la liste des salons
    else:
        form = SignupForm()
    return render(request, 'chat/signup.html', {'form': form})

def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    messages = room.messages.all()
    return render(request, 'chat/room_detail.html', {'room': room, 'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        room_id = request.POST.get('room_id')
        
        if content and room_id:
            room = Room.objects.get(id=room_id)
            # On crée le message en base de données
            new_message = Message.objects.create(
                room=room,
                user=request.user,
                content=content
            )
            # On répond à jQuery que tout s'est bien passé
            return JsonResponse({
                'status': 'success',
                'user': new_message.user.username,
                'content': new_message.content,
                'timestamp': new_message.timestamp.strftime('%H:%M')
            })
    return JsonResponse({'status': 'error'}, status=400)