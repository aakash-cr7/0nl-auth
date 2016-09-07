""" User auth views """

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

import json
import requests
import urlparse

CLIENT_ID = '66dc6d962dce6d4fdd0e'
CLIENT_SECRET = 'b00c4de494ebb7216e91cc01b344a82dcfa7e557'

def linkedin_connect(request):
    """ Store user linkedin credentials """

    html = 'auth/linkedin.html'
    data = {}
    return render(request, html, data)

def github_connect(request):
    """ Store user github credentials """

    html = 'auth/github.html'
    data = {}

    # After authorizing, github sends a code
    if 'code' in request.GET:
        code = request.GET.get('code')
        header = {'content-type': 'application/json'}

        # Send request to github to get user access token
        r = requests.post(
                'https://github.com/login/oauth/access_token', 
                data=json.dumps({
                    'client_id': CLIENT_ID, 
                    'client_secret': CLIENT_SECRET,
                    'code': code
                }),
                headers=header
            )
        # Convert urlencoded response to json
        response_json = json.dumps(urlparse.parse_qs(r.content))
        # Save user access token
        # here
        #
        #
    return render(request, html, data)
