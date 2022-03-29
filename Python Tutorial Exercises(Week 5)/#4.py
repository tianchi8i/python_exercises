'''
use if len(i) >= 8 to find all the strings that have at least 8 characters or more.

use if not sym.isalnum() to get the strings with least one character is not alphanumeric

use if sum(map(str.islower, low)) >= 1 to get the strings with least one character is lowercase letter
use mapfunction you can specify the function then you specify the data to iterate over.
the map function will return an iterator over the collection of str.islower applied to each 'low' value.

use if sum(map(str.isupper, up)) >= 1 to get the strings with least one character is uppercase letter
    
use if sum(map(str.isdigit, num)) >= 2 to get the strings with least two character is numbers

'''

def check_password(andrews_passwords, num):
    if num == 'characters':
        characters = [char for char in andrews_passwords if len(char) >= 8]
        return characters
    elif num == 'symbol':
        symbol = [sym for sym in andrews_passwords if not sym.isalnum()]
        return symbol
    elif num == 'lowercase':
        lowercase = [low for low in andrews_passwords if sum(map(str.islower, low)) >= 1]
        return lowercase
    elif num == 'uppercase':
        uppercase = [up for up in andrews_passwords if sum(map(str.isupper,up)) >= 1]
        return uppercase
    elif num == 'number':
        number = [num for num in andrews_passwords if sum(map(str.isdigit, num)) >= 2 ]
        return number
    elif num == 'strong_passward':
        strong_passward = [num for num in [up for up in [low for low in [sym for sym in [char for char in andrews_passwords if len(char) >= 8] if not sym.isalnum()] if sum(map(str.islower, low)) >= 1] if sum(map(str.isupper,up)) >= 1] if sum(map(str.isdigit, num)) >= 2 ]
        return strong_passward
    
andrews_passwords = ["123456", "hAhA123!", "MyCarR0cks*", "EasyPassword123$$", "AnotherPassword??", "letmein"]

print(check_password(andrews_passwords, 'characters'))
print(check_password(andrews_passwords, 'symbol'))
print(check_password(andrews_passwords, 'lowercase'))
print(check_password(andrews_passwords, 'characters'))
print(check_password(andrews_passwords, 'number'))
print(check_password(andrews_passwords, 'strong_passward'))