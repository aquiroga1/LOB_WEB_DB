from django.shortcuts import render, HttpResponse

# Create your views here.

def center(request):

    return render(request, "ProjetowebApp/center.html")