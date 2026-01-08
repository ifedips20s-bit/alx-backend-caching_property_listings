from django.core.cache import cache
from .models import Property
import logging

def get_all_properties():
    # Try to get the cached queryset
    properties = cache.get('all_properties')
    if properties is None:
        # If not cached, fetch from DB
        properties = list(Property.objects.all())  # convert to list to cache results properly
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    return properties

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    # Get the raw Redis client
    redis_client = cache.client.get_client()
    
    # Fetch INFO stats
    info = redis_client.info()
    
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    
    total_requests = hits + misses
    hit_ratio = hits / total_requests if total_requests > 0 else 0
    
    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio,
    }
    
    logger.error(f"Redis cache metrics: {metrics}")  # log as error instead of info
    
    return metrics
