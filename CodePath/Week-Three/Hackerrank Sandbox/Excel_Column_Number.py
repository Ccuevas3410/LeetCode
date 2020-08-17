 
 
 
 # Complete the 'excel_column_to_number' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING column as parameter.
#
# Given a column as represented in excel, return
# its corresponding column number. 
#


# A-> 1
# B -> 2

# AA -> 27
# AB -> 28
 

def excel_column_to_number(column):
    sum_num = 0
    for i in range(len(column)):
        
          sum_num += (((26 ** i) *  (ord(column[len(column) - i -1]) - 64 )))
    return sum_num

       


print(excel_column_to_number("BA"))