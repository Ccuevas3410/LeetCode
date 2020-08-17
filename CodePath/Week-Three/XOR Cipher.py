word = "H"


print(ord("H") )
print(ord("G") ^ ord('P'))
print(chr(23))
# print(24 ^ ord('P'))
# print(chr(24))




def encryptDecrypt(word, key):


     new_word =  ""
     for i in range(len(word)):
         new_word += chr(ord(word[i])^ ord(key))

     return new_word



print(encryptDecrypt("55;#6?\"55;#","P"))
print(encryptDecrypt("eeksforeeks","P"))


