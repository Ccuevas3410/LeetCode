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


    # newWord = ""
    # for i in range(len(s)):

        #  if s[i].isalpha() and s[i].islower():
        #     if ord(s[i]) + k > 122:
        #          newWord += chr( 96  + (( ord(s[i]) + k)%26))
        #     else:  
        #         newWord += chr(ord(s[i]) + k)


        # #  elif s[i].isalpha() and s[i].isupper():
        # #      if ord(s[i]) + k > 90:
        # #          newWord += chr(64 + (( ord(s[i]) + k) %26))
        # #      else:  
        # #         newWord += chr(ord(s[i]) + k)   
        #  else:
        #      newWord += s[i]

    new_Word = ""
    is_upper = False

    if s.isupper():
        is_upper = True
        s = s.lower()


    for i in range(len(s)):
        curr_char = s[i]
        curr_num = ord(curr_char) - 97
        new_num = (curr_num + k) % 26
        new_char = chr(new_num + 97)
        new_Word+= new_char

    if is_upper:
        return new_Word.upper()
    else:   
         return  new_Word



print(caesarCipher("acf",4))
print(caesarCipher("zcf",25))
print(caesarCipher("alecmori",13))





