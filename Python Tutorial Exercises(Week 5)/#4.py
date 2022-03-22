'''
use if len(i) >= 8 to find all the strings that have at least 8 characters or more.
    characters = [char for char in andrews_passwords if len(char) >= 8]

use if not sym.isalnum() to get the strings with least one character is not alphanumeric
    symbol = [sym for sym in andrews_passwords if not sym.isalnum()]

use if sum(map(str.islower, low)) >= 1 to get the strings with least one character is lowercase letter
    lowercase  = [low for low in andrews_passwords if sum(map(str.islower, low)) >= 1]

use if sum(map(str.isupper, up)) >= 1 to get the strings with least one character is uppercase letter
    uppercase  = [up for up in andrews_passwords if sum(map(str.isupper,up)) >= 1]
    
use if sum(map(str.isdigit, num)) >= 2 to get the strings with least two character is numbers
    number = [num for num in andrews_passwords if sum(map(str.isdigit, num)) >= 2 ]

'''

andrews_passwords = ["123456", "hAhA123!", "MyCarR0cks*", "EasyPassword123$$", "AnotherPassword??", "letmein"]

def check_password(andrews_passwords):

    final = [num for num in [up for up in [low for low in [sym for sym in [char for char in andrews_passwords if len(char) >= 8] if not sym.isalnum()] if sum(map(str.islower, low)) >= 1] if sum(map(str.isupper,up)) >= 1] if sum(map(str.isdigit, num)) >= 2 ]
    return final

print(check_password(andrews_passwords))
