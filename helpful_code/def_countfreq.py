def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c]+=1
    return d
    
