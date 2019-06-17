from django.shortcuts import render


def labApp(request):
    return render(request, 'lab.html')
