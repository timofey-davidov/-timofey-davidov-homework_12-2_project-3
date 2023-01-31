def get_val(collection, key, default='git'):
    if key not in collection.keys():
        return default
    return collection[key]