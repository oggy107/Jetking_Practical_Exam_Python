# Write a Python Program to remove the duplicate elements of a
# given array of numbers such that each element appear only once
# and return the new length of the given array.

# NOTE: I have created three different functions to remove the duplicate elements from array and return its new length

def removeDuplicate(array: list) -> int:
    # we can typecast list (array) into a set and then return its length

    array = set(array)
    return len(array)

def alterante(array: list) -> int:
    # removing the duplicate elements from the list using count method

    for i in array:
        if array.count(i) > 1:
            array.remove(i)

    return len(array);

def alternateSecond(array: list) -> int:
    # selecting index i and then iterating upon remaining list using index j and if element
    # at index i is equal to element at index j then we remove element at that index thus removing all duplicate elements

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if (j >= len(array)):
                break
            if array[i] == array[j]:
                array.remove(array[j])

    return len(array);

print(removeDuplicate([1, 3, 3, 4, 5, 6])) # output: 5
print(removeDuplicate([1, 2, 3, 4, 5, 6])) # output: 6
print(removeDuplicate([4, 2, 3, 4, 5, 4])) # output: 4

print(alterante([1, 3, 3, 4, 5, 6])) # output: 5
print(alterante([1, 2, 3, 4, 5, 6])) # output: 6
print(alterante([4, 2, 3, 4, 5, 4])) # output: 4

print(alternateSecond([1, 3, 3, 4, 5, 6])) # output: 5
print(alternateSecond([1, 2, 3, 4, 5, 6])) # output: 6
print(alternateSecond([4, 2, 3, 4, 5, 4])) # output: 4