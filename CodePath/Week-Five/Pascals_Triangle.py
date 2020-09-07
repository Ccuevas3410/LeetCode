# Given N  
# return a 2D array that represents the first N rows of Pascal's Triangle
# To get the Nth row of pascal's triangle,
# the first and last value are always 1
# the value of row[i] is the sum of the value of the previous row at i, and the the value of the previous row at i-1
## for example:
N = 3
# return:
[
  [1],
  [1,1],
  [1,2,1],
]

N = 7
# return:
[
  [1],
  [1,1],
  [1,2,1],
  [1,3,3,1],
  [1,4,6,4,1],
  [1,5,10,10,5,1],
  [1,6,15,20,15,6,1]
]

## (Scroll down for optional help , stretch questions, and useful links)
def print_formatted(triangle):
    print("------")
    for row in triangle:
        printable_row = ""
        for column in row:
            printable_row+= str(column)
        print(printable_row)
    print("------")

def pascals_triangle(n):

    if n < 1 :
        return [[]]

    triangle = []
    current_row = [1]
    triangle.append(current_row)

    for i in range(n-1):
        next_row = []
        next_row.append(1)

    # if n == 1:
    #     triangle.append([1])
    #     return triangle

    # elif n == 2 :
    #     triangle.append([[1],[1,1]])
    #     return triangle
    # else:
    #     triangle.append([[1],[1,1]])
    #     for row in range(3,n):
    #         for column in range(1,n):

    #         triangle.append([,])

        for column in range(len(current_row)-1):
            next_element = current_row[column] + current_row[column+1]
            next_row.append(next_element)


        next_row.append(1)
        triangle.append(next_row)
        current_row = next_row
    return triangle
    
           


  



print_formatted(pascals_triangle(5))