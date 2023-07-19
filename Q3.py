# Q3. Write a Python Program to check whether a given integer is a palindrome or not.
# Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindrome.

def isPalindrome(number: int) -> bool:
    # returning False if number is negative accoring to the note
    if (number < 0):
        return False

    # reversing the number and comparing it to the original number and returning True if they are equal else False
    return True if str(number)[::-1] == str(number) else False

print(isPalindrome(121121)) # output: True
print(isPalindrome(1213)) # output: False
print(isPalindrome(321)) # output: False