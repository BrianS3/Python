def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far
