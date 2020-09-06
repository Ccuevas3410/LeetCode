def reverse_int(integer):
    newInt = str(integer)
    positive = True

    if newInt[0] == "-":
        positive = False

    if  newInt[-1] == "0":
        if not positive:
            newInt ="-" + newInt[-2:0:-1]
        else:
           newInt =  newInt[::-1]

    else:
        if not positive:
            newInt ="-" + newInt[-1:0:-1]
        else:
            newInt = newInt[::-1]


    if  int(newInt).bit_length() > 32:
         return 0

    return int(newInt)


print(reverse_int(123))