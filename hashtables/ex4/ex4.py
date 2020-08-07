def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    counter = {}
    result = []

    for element in a:
        counter[element] = 1

    for element in a:
        if -(element) in counter:
            #print(element)
            result.append(element)
            

    
    
    new_result = []
    for item in result:
        if item > 0:
            print(item)
            new_result.append(item)

    print(new_result)
    return new_result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
