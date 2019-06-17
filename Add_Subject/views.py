from django.shortcuts import render

# Create your views here.


def subApp(request):
    return render(request, 'Sub.html')