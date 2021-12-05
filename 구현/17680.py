def solution(cahceSize, cities):
    if cahceSize == 0:
        return 5 * len(cities)
    cache = []
    time = 0
    while cities:
        city = cities.pop().lower()
        if city in cache:
            idx = cache.index(city)
            if idx != len(cache) - 1:
                cache = cache[:idx] + cache[idx + 1 :] + [city]
            time += 1
            continue
        time += 5
        if len(cache) < cahceSize:
            cache.append(city)
        else:
            cache = cache[1:]
            cache.append(city)
    return time
