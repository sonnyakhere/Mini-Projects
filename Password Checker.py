import re
import string
import random


#Setting password length
passwd_len = list(range ( 6 , 20 , 1 ))

#Function to suggest random password
def suggest_random():
    length = random.choice(passwd_len)
    random_passwd = []
    n = 0

#Generate random password containing required characters
    while n <= length:
        random_passwd += random.choice(string.ascii_lowercase)
        n += 1
        random_passwd += random.choice(string.ascii_uppercase)
        n += 1
        random_passwd += random.choice(string.digits)
        n += 1
        random_passwd += random.choice('!@#$%^&*()_-')
        n += 1

    list_random_passwd = list(random_passwd)
    random.SystemRandom().shuffle(list_random_passwd)
    print("".join(list_random_passwd))
    
    return interaction()


#Function of response everytime password is invalid
def response():
    print('Password must be atlease 6-20 characters long, contain uppercase, lowercase, a number and a symbol, try again.')
    response = input('Would you like a password suggestion Y/N? ')
    if response == 'Y':
        print('Try this Password:')
        suggest_random()
    elif response == 'N':
        return
    else :
        print('Invalid Input')


#Function to request and validate password
def interaction():
    while True:
        passwd = input('Input a Password:')
        if len(passwd)<6 or len(passwd)>20:     #check length is between 6-20 characters
            response()
        
        elif not re.search('[a-z]', passwd):    #check it contains lowercase
            response()
        
        elif not re.search('[A-Z]', passwd):    #check it contains uppercase
            response()

        elif not re.search('[0-9]', passwd):    #check it contains digits
            response()
        
        elif not re.search('[!@#$%^&*()_-]', passwd):   #check it contains special characters
            response()
        
        elif re.search('[ ]', passwd):          #check it doesn't contain spaces
            print('Spaces are not allowed, try again.')
        
        else:
            print('Valid Password.')
            break
    return exit()

interaction()