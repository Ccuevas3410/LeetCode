def right_triangle(n):
    triangle_array =[]

    for row in range(n+1):
        current_row = [0] * (row) 
        triangle_array.append(current_row )
    
    return triangle_array 

print(right_triangle(5))

def print_formatted(triangle):
    print("------")
    for row in triangle:
        printable_row = ""
        for column in row:
            printable_row+= str(column)
        print(printable_row)
    print("------")

print_formatted(right_triangle(5))