# Complete the 'atoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
# The function will convert the string parameter 
# into an integer, and return the result. 
#
#

# # Example  1
# Input: "42"
# Output: 42


# # Example  2
# Input: "-42"
# Output: -42


def atoi(a):
    
    #First, we clean up the integer

    a = a.strip()
    sign = 1

    if len(a) == 0:
     return 0

#Then we check for the sign

    newNum = 0
    sign = -1 if a[0] == "-" else 1
    start = 1 if a[0] in "-+" else 0

    int_max_min =  0 - 2**31  if sign == "+" else 2**31 - 1

    for i in range(start,len(a)):


        #Turn string into number
        string_to_num = ord(a[i])

        if string_to_num < 48 or string_to_num > 57:
                break

        newNum *= 10
        newNum +=  string_to_num - 48

        if newNum >= int_max_min :
            newNum = int_max_min
            break

    return sign * newNum


    # newNum = ""
    # sign = ""
    # for i in range(len(a)):

    #     if  a[0] != "-" or a[0] != "+":
    #         if 
    #         return 0

    #     if a[i].isnumeric():
    #         newNum+= a[i]
    #     elif a[i] == "-" or a[i] == "+":
    #         sign += a[i]
    #     else:
    #         continue
    # return int(sign+newNum)



print(atoi("        -42"))
