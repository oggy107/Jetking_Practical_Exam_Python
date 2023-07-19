# Q2. Write a Python Program to reverse only the vowels of a given string.

def revVowels(string: str) -> str:
    string = list(string)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    strVowels = []
    strIndex = []

    # we need to store vowels and their index in a list to reverse the vowels
    # and later modify original string using reversed vowels and their positions stored in strIndex

    # storing the vowels in a list and their index in another list
    for i in range(len(string)):
        if string[i] in vowels:
            strVowels.append(string[i])
            strIndex.append(i)

    # reversing the vowels
    strVowels = strVowels[::-1]

    # replacing the vowels with the reversed vowels
    for i in range(len(strVowels)):
        string[strIndex[i]] = strVowels[i]

    return ''.join(string)

print(revVowels('Hello')) # output: Holle
print(revVowels('Hello World')) # output: Hollo Werld