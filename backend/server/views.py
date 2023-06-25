import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from dotenv import load_dotenv

load_dotenv()


# Create your views here.

def home(request):
    return HttpResponse("Welcome to ur home page")


def user_details(request):
    return HttpResponse("These are ur details")


def user_interests(request):
    return HttpResponse("ooh noice interests!")


def api_view(request):
    # Make a request to the IEEE API

    base_url = "https://api.springernature.com/meta/v2/json"
    # API key
    api_key = os.environ.get('SPRINGER_API_KEY')
    params = {
        "q": 'Papers+Artificial+Intelligence',
        "api_key": api_key
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed

        # Return a JSON response to the client
        return JsonResponse({'data': data})

    # If the request failed, return an error response
    return JsonResponse({'error': 'Failed to retrieve data from IEEE API'})
