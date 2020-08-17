# Complete the 'isPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
# Check if a is a palindrome and return 1 if it
# is a palindrome and 0 if it is not. 
#
#

def isPalindrome(a):

     a = a.strip().lower()

     cleaned_string = ""

     for i in range(len(a)):
         if a[i].isalpha():
             cleaned_string += a[i]

     if cleaned_string == cleaned_string [::-1]:
        return True

     return False




print(isPalindrome("Race Car"))