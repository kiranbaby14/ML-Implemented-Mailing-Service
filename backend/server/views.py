import json
import os
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import re
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


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Tag, UserTagPreference, TagLabels


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_user_tag_preference(request):
    tag_ids = eval(str(request.data))

    # Clear existing user tag preferences
    request.user.usertagpreference_set.all().delete()

    # Concatenate tag IDs into a single string
    tags_text = ', '.join([json.dumps(item) for item in tag_ids])
    tag_labels_text = ', '.join([json.dumps(item["label"]) for item in tag_ids if item["variant"] == ''])

    # Get all tags that are not associated with any UserTagPreference objects
    unused_tags = Tag.objects.exclude(usertagpreference__isnull=False)
    unused_tag_labels = TagLabels.objects.exclude(usertagpreference__isnull=False)

    # Delete the unused tags and tag_labels
    unused_tags.delete()
    unused_tag_labels.delete()

    # Create a single Tag instance with the concatenated tags
    tag = Tag(tags=tags_text)
    tag.save()

    # Create a single TagLabels instance with the concatenated tag_labels
    tag_labels = TagLabels(labels=tag_labels_text)
    tag_labels.save()

    # Create UserTagPreference instance
    UserTagPreference.objects.create(user=request.user, tag=tag, tag_labels=tag_labels)

    return Response({'message': 'User tag preferences saved.'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_tag_preference(request):
    user = request.user

    # Retrieve the user's tag preferences
    tag_preferences = UserTagPreference.objects.filter(user=user)

    # Extract the tag names from the preferences
    tag_names = [preference.tag.tags for preference in tag_preferences]

    tag_names = re.findall(r'{[^}]+}', tag_names[0])
    tag_names = [json.loads(dicti) for dicti in tag_names]
    return Response(tag_names)
