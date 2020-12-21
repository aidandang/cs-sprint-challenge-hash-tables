def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    buckets = {}

    result = []

    for i in a:
        buckets[str(i)] = i

    for i in a:
        if i > 0:
            if ('-' + str(i)) in buckets:
                result.append(i)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
