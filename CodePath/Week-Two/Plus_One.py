#
# Complete the 'plusOne' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY digits as parameter.
# This function will take the value represented by the 
# array digits, add 1 to it, and return the resulting 
# array. 
def plusOne(digits):
        carry = 1


      
        for i in range(-1, -1 - (len(digits)), -1):



                    if digits[i] == 9 and carry == 1:
                        digits[i] = 0
                    

                    elif carry > 0:
                        digits[i] += 1
                        carry = 0


        if carry > 0:
                digits[0] += 1

        return digits




digits =[2,9,9,9,9]
print(plusOne(digits))