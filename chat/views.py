from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse
from .forms import SignupForm, RoomForm
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

def get_messages(request, room_id):
    # On récupère l'ID du dernier message que le navigateur possède déjà
    last_id = request.GET.get('last_id', 0)
    
    # On ne filtre que les messages de cette room dont l'ID est supérieur au dernier reçu
    messages = Message.objects.filter(room_id=room_id, id__gt=last_id).order_by('timestamp')
    
    results = []
    for m in messages:
        results.append({
            'id': m.id, # Crucial pour le prochain appel !
            'user': m.user.username,
            'content': m.content,
            'timestamp': m.timestamp.strftime('%H:%M')
        })
    
    return JsonResponse({'messages': results})

@login_required
def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') # <--- Renvoie à l'accueil automatiquement
    else:
        form = RoomForm()
    return render(request, 'chat/create_room.html', {'form': form})

@login_required
def delete_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    # On vérifie que c'est bien le créateur ou l'admin
    if room.creator == request.user or request.user.is_staff:
        room.delete()
    return redirect('index')