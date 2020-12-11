
palindrome = "abcdcba"

#def palindrome_check(string):
#    if type(string) != None:
#        if string == string[::-1]:
#            return True
#        return False
#
#print(palindrome_check(palindrome))



# Optimized:

def isPalindrome(string):
    right = 0
    left = len(string)-1
    while right < left:
        if string[right] != string[left]:
            return False
        right += 1
        left -= 1
    return True

print(isPalindrome(palindrome))