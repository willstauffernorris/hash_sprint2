        #Given a package with a weight limit limit 
    #a list weights of item weights
    # implement a function get_indices_of_item_weights
def get_indices_of_item_weights(weights, length, limit):
    """
    finds two items whose sum of weights equals the weight limit limit. 
    will return a tuple of integers that has the following form:

    (zero, one)

    The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index. 
    If such a pair doesn’t exist for the given inputs, your function should return None.
    """
    # Your code here

    #where does weights[x] + weights[y] == limit?

    # make a lookup

    weight_dict = {}

    if length == 1:
        return None
    else:
        for i in range(len(weights)):
            
            item = weights[i]
            #if item in weight_dict:
                #print(i)
                #print(item)
                #weight_dict[item].insert(0,i)
            #else:
            weight_dict[item] = i
   # print(weight_dict)

    for item in weights:
        
        if (limit - item) in weight_dict:
            #print(weight_dict[limit-item])
            #print('FOUND ONE')
            return_value = [weight_dict[limit-item], weights.index(item)]
            return return_value



        # start over
    # else:
    #     for item in weights:
    #         for second_item in weights:
    #             print(item, second_item)
    #             if item + second_item == limit:
    #                 if second_item >= item:
    #                     print('wtf')
    #                     print([weights.index(second_item), weights.index(item)])
    #                     return [weights.index(second_item), weights.index(item)]
    #                 else:
    #                     print(item, second_item)
    #                     #print([weights.index(item), weights.index(second_item)])
    #                     return [weights.index(item), weights.index(second_item)]
    #             # else:
    #             #     return None

    
                
    #return None


    # if x + y == limit:
        # return x, y
    # else:
    #     return None


    # two_items = (weights[x], weights[y])
    # return two_items

#test
#get_indices_of_item_weights(weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21)


#output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
