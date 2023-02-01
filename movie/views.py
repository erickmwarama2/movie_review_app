from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1> Welcome Home </h1>')


def about(request):
    return HttpResponse('<h3> About Us </h3>')


def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {
        'name': 'Erick Mutwiri',
        'searchTerm': searchTerm
    })

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
