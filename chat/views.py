from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignupForm
from .models import Room, Message



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


@login_required # Outil natif : redirige vers la connexion si non identifié
def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = room.messages.all()
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'messages': messages
    })


@login_required
def flag_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(Message, id=message_id)
        message.is_flagged = True # On marque le message pour modération
        message.save()
        # Redirige vers le salon où se trouvait le message
        return redirect('room_detail', slug=message.room.slug)