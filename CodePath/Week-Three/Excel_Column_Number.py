def titleToNumber(s) :
        
        
     sum = 0
     for i in range(0 ,len(s)):

      
          sum += (( 26 ** ((len(s) - 1) - i) ) *  (ord(s[i]) - 64 ))

     print(sum)         


       
titleToNumber("BDA")

    

     # s = s [::-1]
     
     #  sum = 0
     #  for i in range(0 ,len(s)):

      
     #           sum += ( (26 ** i) *  (ord(s[i]) - 64 ))
        
     #  return sum