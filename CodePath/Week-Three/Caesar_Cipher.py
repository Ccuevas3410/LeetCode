# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
#  In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

# input
# middle-Outz
# 2

# Sample Output
# okffng-Qwvb

def caesarCipher(s, k):


    newWord = ""
    for i in range(len(s)):

         if s[i].isalpha() and s[i].islower():
            if ord(s[i]) + k > 122:
                 newWord += chr( 96  + (( ord(s[i]) + k)%26))
            else:  
                newWord += chr(ord(s[i]) + k)


        #  elif s[i].isalpha() and s[i].isupper():
        #      if ord(s[i]) + k > 90:
        #          newWord += chr(64 + (( ord(s[i]) + k) %26))
        #      else:  
        #         newWord += chr(ord(s[i]) + k)   
         else:
             newWord += s[i]

    return newWord


print(caesarCipher("middle-Outz",2))


print((ord("t") + 2) % 26)

print(chr(97+14))



