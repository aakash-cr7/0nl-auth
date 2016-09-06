""" User auth views """

from django.shortcuts import render, get_object_or_404

def linkedin_connect(request):
    """ Store user linkedin credentials """

    html = 'auth/linkedin.html'
    data = {}
    pass
    return render(request, html, data)

def github_connect(request):
    """ Store user github credentials """

    html = 'auth/github.html'
    data = {}
    pass
    return render(request, html, data)
