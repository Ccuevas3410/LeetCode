
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


# U - > We need to return the roman number in decimals
# M -> Dict to store the roman numbers and their equivalents in decimals
# P - > The plan is to iterate trough the string and check for special cases where a roman is before another
# I -> Done
# R -> 
# E -> Run Time = , Space Complexity = 




def romanToInt(s):

  romans = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  sum = 0
 
  
  for i in range(1,len(s)):
    
      if s[i-1] == "I" and (s[i] == "V" or  s[i] == "X"):
          sum += (romans[s[i]]   - romans[s[i-1]])
          continue
      if s[i-1] == "X" and (s[i] == "L" or  s[i] == "C"):
         sum += romans[s[i]]-romans[s[i-1]]
         continue
          
      if s[i-1] == "C" and (s[i] == "D" or  s[i] == "M"):
          sum += romans[s[i]] - romans[s[i-1]]
          continue
      
      else:
         sum += romans[s[i]]
    
    
    
 
  
  
  return (sum )
    
    
print(romanToInt("CM"))
  
    