from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm
from apps.userprofile.models import Userprofile

def frontpage(request):
    return render(request, "core/frontpage.html")


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')


def plans(request):
    return render(request, 'core/plans.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user=user)
            login(request, user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})
