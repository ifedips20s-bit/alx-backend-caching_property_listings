from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get the cached queryset
    properties = cache.get('all_properties')
    if properties is None:
        # If not cached, fetch from DB
        properties = Property.objects.all()
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    return properties
