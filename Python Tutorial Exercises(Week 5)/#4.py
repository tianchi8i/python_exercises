'''
use of len(password) < 8 to find all the strings that are less than 8 characters (we don't want them so return False others go to the next filter)

use password.isalnum()  to check if all characters in the string are alphanumeric or not. 
it turns True if all characters in the string are alphanumeric (We wanted the strings with at least one Symbol so return False go to the next filter)

use isalpha() if to check if all characters in the string are alphabetic or not. 
it turns True if all characters in the string are alphabetic 
(We wanted the strings with symbols and alphanumeric so return False go to the next filter)

use if password.islower(): to get the strings with least one character is uppercase letter.
The islower() method returns True if all the characters are in lower case, otherwise False.
(We dont know the password to be all the characters are in lower case, so return False go to the next filter)

use if password.isupper(): to get the strings with least one character is uppercase letter.
The isupper() method returns True if all the characters are in upper case, otherwise False.
(We dont know the password to be all the characters are in upper case, so return False go to the next filter)
    
use if (sum(c.isdigit() for c in password) < 2): to check if the strings/password has at least 2 number turn True other False.

'''
def check_password(password):
    if len(password) < 8:
        return False

    if password.isalnum():
        return False

    if not any(c.isalpha() for c in password):
        return False

    if password.islower():
        return False

    if password.isupper():
        return False

    if (sum(c.isdigit() for c in password) < 2):
        return False

    return True

andrews_passwords = ["123456", "hAhA123!", "MyCarR0cks*", "EasyPassword123$$", "AnotherPassword??", "letmein"]
print([password for password in andrews_passwords if check_password(password)])