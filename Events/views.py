from django.shortcuts import render


def eventApp(request):
    return render(request, 'event.html')