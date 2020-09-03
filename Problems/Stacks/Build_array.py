

# Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

# Build the target array using the following operations:

# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

# Return the operations to build the target array.

# You are guaranteed that the answer is unique.

# Example 1:
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: 
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]

# Example 2:

# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]


#USING ARRAY
# def buildArray( target ,n):
#     newArr = []

#    x = []
#         a = max(target)
#         for i in range(1,n+1):
#             if i<=a:
#                 if i in target:
#                     x.append("Push")
#                 else:
#                     x.append("Push")
#                     x.append("Pop")
#         return x



#print(buildArray([1,3],3))
#print(buildArray([1,2],4))
#print(buildArray([3,4,5,6,8,9],9))

#USING STACK

def buildArray( target ,n):
      stack = [ n for n in range(n,0,-1)]
      answer = []
      

      while stack:
        number = stack.pop()
        
        if number > target[-1]:
            return answer
        elif  number in target :
            answer.append("Push")
            
        else:
             answer.append("Push")
             answer.append("Pop")
             
      return answer


     
print(buildArray([1,2],4))
#print(buildArray([3,4,5,6,8,9],9))