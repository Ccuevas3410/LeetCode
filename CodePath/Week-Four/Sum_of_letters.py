
#
# Complete the 'summate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING vals as parameter.
# The function will summate the ASCII values of
# the characters in the string it accepts as a
# parameter. 
#

def summate(vals):

  if not vals:
      return 0
      
  sum = 0

  for i in vals:
      sum += ord(i)

  return sum
print(summate("hi"))
