 
 
 
#  A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.


# Example 1:

# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
 

 #Works but not for 2 several parenthesis inside each other
# def removeOuterParentheses(S):



#     count = 0

    
#     for i in range(len(S)):

#         if S[i] == "(" and S[i+1]==")":
#             count+=1
#         else:
#             continue
#     return "()" * count

# print(removeOuterParentheses("(()())(())"))
# print(removeOuterParentheses("(()())(())(()(()))"))

def removeOuterParentheses(S):
    stack = []
    answer = []

    for i in S:
        if not  stack:
            stack.append(i)
        elif i == ")":
            stack.pop()
            if  stack:
                answer.append(i)
        else:
            stack.append(i)
            answer.append(i)

    return "".join(answer)

print(removeOuterParentheses("(()())(())(()(()))"))