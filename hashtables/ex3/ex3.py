def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    my_dict = {}
    result = []

    for array in arrays:
        for item in array:
            if item in my_dict:
                my_dict[item] += 1
                #print("ITEM FOUND")
            else:
                my_dict[item] = 1
        

    for key, value in my_dict.items():
        if value > 1:
            #print(key)
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(100, 200)) + [1, 2, 3])
    arrays.append(list(range(200, 300)) + [1, 2, 3])
    arrays.append(list(range(300, 400)) + [1, 2, 3])

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
