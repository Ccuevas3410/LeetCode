#
# Complete the 'brickBreak' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING bricks
#  2. INTEGER ball
# This function will check the string at the 
# index specified by the ball. If there is a
# brick ("-") in that index, it will be replaced
# with a space. Otherwise, nothing will be altered. 
#

def brickBreak(bricks, ball):
    
    new_bricks = ""
    

    if bricks[ball] == "-":
        new_bricks = bricks[:ball] + " " + bricks[ball + 1:]

    return  new_bricks




#OR 

# def brickBreak(bricks, ball):
    
#     new_bricks = list(bricks)
    

#     if new_bricks[ball] == "-":
#         new_bricks[ball] = " "

#     return  "".join(new_bricks)




print(brickBreak(" ---- -",2))
        