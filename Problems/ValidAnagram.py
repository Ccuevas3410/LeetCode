
def isAnagram( s, t) -> bool:
        dictOne = {}
        dictTwo={}
        
        print('HELLO')
        for i in range(len(s)):
            if s[i] in dictOne:   
                dictOne[s[i]]+=1
                print('HELLO1')
            else:
                dictOne[s[i]] =1
                
            
        for j in range(len(s)):
            if t[j] in dictTwo:
                dictTwo[t[j]]+=1
               
                print('HELLO3')
            else:
                dictTwo[t[j]]=1

        for x in range(len(dictOne)):
            if s[x] in dictTwo and dictOne[s[x]] == dictTwo[s[x]]:

                print("TRUE")    
            else:
                print("FALSE")    


        
               
       

isAnagram('anagram','nagaram')