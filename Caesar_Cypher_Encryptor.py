## Caesar_Cypher_Encryptor

string = "xyz"


def caesarCipherEncryptor(string, key):
    new_string = ""
    for char in string:
        if char.islower() and type(key) == int:
            char_index = ord(char) - ord("a")
            new_index = (char_index + key) % 26
            encoded_char = new_index + ord("a")
            new_char = chr(encoded_char)
            new_string = new_string  + new_char
        else:
            char_index = ord(char) - ord("A")
            new_index = (char_index + key) % 26
            encoded_char = new_index + ord("A")
            new_char = chr(encoded_char)
            new_string = new_string  + new_char

    return new_string

    
string2 = "JGSJVVJXVAzzdclaskdjcnjn"

print(caesarCipherEncryptor(string2, 2))




##### OPTIMIZED BUT INCOMPLETE:
####def caesarCipherEncryptor(string, key):
####    new_string = ""
####    abc = list("abcdefghijklmnopqrstuvwxyz")
####    new_key = key % 26
####    #string = string.lower()
####    for i in string:
####        if i.islower() and type(key) == int:
####            #i_index = ord(i) - ord("a")
####            #new_index = (i_index + key) % 26
####            #encoded_char = new_index + ord("a")
####            #new_char = chr(encoded_char)
####            new_string = new_string  + getNewChar(i, new_key, abc)
####        else:
####            new_string += i
####    return new_string
####
####def getNewChar(char, key, abc):
####    encoded_char = abc.index(char) + key
####    return abc[encoded_char] if encoded_char <= len(abc)-1 else abc[0] 

    