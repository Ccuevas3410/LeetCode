def titleToNumber(s) :
        
        
      s = s [::-1]
     
      sum = 0
      for i in range(0 ,len(s)):

      
               sum += ( (26 ** i) *  (ord(s[i]) - 64 ))
            
      print (sum)         


       
       

print(titleToNumber("BDF"))