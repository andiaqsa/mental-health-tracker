from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275046',
        'name': 'Andi Aqsa',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
