def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # initiate a hash table
    buckets = {}

    pair = []
    
    # put weights list to the hash table by coverting value of the weight list to key and new value is (limit - current)
    for w in weights:
        key = str(w)
        buckets[key] = limit - w

    # check there is an existed key in the buckets where value equal (limit - current)
    for i in range((length - 1), -1, -1):
        key = str(weights[i])
        value = buckets[key]
        if str(value) in buckets:
            pair.append(i)

    if pair != []:
        return tuple(pair)

    return None
