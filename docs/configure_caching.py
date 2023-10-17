# settings.py
CACHE_TIMEOUT = int(env("CACHE_TIMEOUT", default=300))  # 300sec -> 5min
if ENV in ("prod", "production") or env("USE_EXTERNAL_CACHE") == "True":
    CACHE_BACKEND = env("CACHE_BACKEND", default="django.core.cache.backends.db.DatabaseCache")
    CACHE_LOCATION = env("CACHE_LOCATION", default="lrbc_cache_table")
    CACHES['default'] = {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION,
        'TIMEOUT': CACHE_TIMEOUT
    }


# in views.py

    # Only allow 'GET' HTTP method
    link = cache.get(code)

    if not link:
        link = Link.objects.filter(shortCode=code).first()
        if not link:
            return HttpResponse("Nothing Found.", status=404)

        cache.set(key=code, value=link, timeout=CACHE_TIMEOUT)

    if not link.active:
        return HttpResponse("URL Not Active.", status=403)

