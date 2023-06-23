from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests


# Create your views here.

def home(request):
    return HttpResponse("These are ur details")


def user_details(request):
    return HttpResponse("These are ur details")


def user_interests(request):
    return HttpResponse("ooh noice interests!")


def ieee_api_view():
    # Make a request to the IEEE API

    # API key
    api_key = 'YOUR_API_KEY'

    # Base URL for the API
    base_url = 'https://ieeexploreapi.ieee.org/api/v1/search/articles'

    # Query parameters
    query_params = {
        'apikey': api_key,
        'format': 'json',
        'max_results': 10,  # Adjust as per your requirements
        'start_record': 1,
        'sort_order': 'desc',
        'sort_field': 'article_number',
        'querytext': 'YOUR_TOPIC'  # Specify your topic here
    }

    # Make the API request
    response = requests.get(base_url, params=query_params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed

        # Return a JSON response to the client
        return JsonResponse({'data': data})

    # If the request failed, return an error response
    return JsonResponse({'error': 'Failed to retrieve data from IEEE API'})
