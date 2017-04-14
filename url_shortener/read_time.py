from django.conf import settings
from django.core.cache import caches

def run(request, cache_name):
    if cache_name == 'random':
        cache_name = random.choice(settings.CACHE_NAMES)
    cache = caches[cache_name]
    t0 = time.time()
    data = cache.get('benchmarking', [])
    t1 = time.time()
    if random.random() < settings.WRITE_CHANCE:
        data.append(t1 - t0)
        cache.set('benchmarking', data, 60)
    if data:
        avg = 1000 * sum(data) / len(data)
    else:
        avg = 'notyet'
    # print(cache_name, '#', len(data), 'avg': avg, 'size:', len(str(data)))
    return http.HttpResponse('{}\n'.format(avg))
