def clean_string(sentence):

    new_sentence  = ""

    for i in sentence:
        if i.isalpha():
           new_sentence += i

    return new_sentence.lower()


def isPalindrome(sentence):
    cleaned_string= clean_string(sentence)

    if cleaned_string == cleaned_string[::-1]:
        return 1
    else:
        return 0
        


print(isPalindrome("Able was I ere I saw Elba"))
print(isPalindrome("A man, a plan, a canal – Panama"))
