from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)  # Still cache the view response for 15 minutes
def property_list(request):
    # Use the low-level cached queryset
    properties = get_all_properties().values()  # Convert queryset to dictionaries
    data = list(properties)
    return JsonResponse({"data": data})