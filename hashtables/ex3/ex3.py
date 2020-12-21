def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    buckets = [None] * len(arrays)

    for i in range(len(arrays)):
        buckets[i] = {}
        for e in arrays[i]:
            buckets[i][str(e)] = e

    exist = False

    intersection_list = []

    i = 1

    for e in arrays[0]:
        j = 1
        while j < len(arrays):
            if str(e) in buckets[j]:
                exist = True
            else:
                exist = False
            j += 1
        if exist == True:
            intersection_list.append(e)
            exist == False

    return intersection_list

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
