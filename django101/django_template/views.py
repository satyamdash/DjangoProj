from django.shortcuts import render

# Create your views here.

def t101(request):
    return render(request, 'django_template/101.html')
