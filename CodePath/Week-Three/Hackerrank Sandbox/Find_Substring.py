# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
# The function will check if str1 is a substring 
# of str2 and return true or false accordingly. 
#

def isSubstring(str1, str2):
    

    if str1 in str2:
        return True

    return False

print(isSubstring("zzz","zzeeezz"))