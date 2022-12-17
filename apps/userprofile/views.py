from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from apps.userprofile.models import Userprofile



@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


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

    return render(request, 'userprofile/signup.html', {'form': form})
