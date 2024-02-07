def linear_search(list, target):
    """
    Return the index postion of the target if found, else return None
    """
    for i in range(0, len(list)): # len(list) -> constant time operation O(1)
        if list[i] == target:
            return i
        return None


def varify(index):
        if index is not None:
            print("Target found at index: ", index)
        else:
            print("Target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
varify(result)
