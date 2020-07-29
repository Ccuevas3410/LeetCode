def first_missing_positive_integer(integers):

#Create empty list , set everything to false

 found_integers = []

 # For every number in the input list

 for integer in integers:
 #if the number is smaller than 0, continue, keep going
    if integer < 0 :
        continue

 #if number is bigger than current length of list, resize the list
    if integer + 1 > len(found_integers):
        #Extend len of list
        extend_size = integer - len(found_integers) +1
        found_integers.extend([False]*extend_size)
    #Set the value of the place in the list with said integer to true
    found_integers[integer] = True 

 missing_int = 0
#Ignore 0 index, make range of the len of found_integers, this turns i into a number iterator
 for i in range(1, len(found_integers)):
   
   ##If the value at i position is false, this tells us the first positive integer
    if found_integers[i] == False:
        missing_int = i
        return missing_int
##If the missing int got turned into a 0    
 if missing_int == 0 and len(found_integers) == 0:
        return 1
 elif missing_int == 0 and len(found_integers) > 0:
    return len(found_integers) 

    

print(first_missing_positive_integer([3,4,-1,1]))