def most_frequent_item_count(collection):
    # Do your magic. :)
    
    check = 0
    nmax = 0
    nset = set(collection)
    
    for i in nset:
        check = collection.count(i)
        
        if check > nmax:
            nmax = check
        
    return nmax
    
    