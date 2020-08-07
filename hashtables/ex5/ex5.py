# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    path_cache = {}

    result = []

    ## split files on /
    ## everything in the last one is the file name
    for item in files:
        split_item = item.split("/")
        file_name = split_item[-1]
        path_name = split_item[:-1]
        path_name = "/".join(path_name)
        #print(f'file name: {file_name}')
        #print(f'path name: {path_name}')
    ## save it in a dictionary with they key as file name, value as path
        if file_name in path_cache:
            #do something
            pass
            path_cache[file_name].append(path_name)
        else:
            path_cache[file_name] = [path_name]
    ## check the queries against the dictionary
    #print(path_cache)
    for item in queries:
        if item in path_cache:
            print(item)
            #print(path_cache[item])
            for i in range(len(path_cache[item])):
                result.append(path_cache[item][i]+"/"+item)
            #result.append(path_cache[item][1]+"/"+item)

    #print(path_cache)
    #print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/user/bin/baz',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
