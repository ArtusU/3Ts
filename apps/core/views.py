from django.shortcuts import render


def frontpage(request):
    return render(request, "core/frontpage.html")


def privacy(request):
    return render(request, 'core/privacy.html')