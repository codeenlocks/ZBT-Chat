from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

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