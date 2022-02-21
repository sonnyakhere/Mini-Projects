import re
import string
import random


characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()")
passwd_len = list(range ( 6 , 20 , 1 ))


def suggest_random():
    length = random.choice(passwd_len)
    random_passwd = []

    def inner_suggest_passwd():
        for i in range(length):
            random_passwd.append(random.choice(characters))
        

    while True:
        inner_suggest_passwd()
        if set(list(string.ascii_lowercase)) & set(random_passwd) != [] and \
            set(list(string.ascii_uppercase)) & set(random_passwd) != [] and \
                set(list(string.digits)) & set(random_passwd) != [] and \
                    set(list('!@#$%^&*()_-')) & set(random_passwd) != []:
            break
        else:
            suggest_random()
    print("".join(random_passwd))
    interaction()
    return



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


def interaction():
    while True:
        passwd = input('Input a Password:')
        if len(passwd)<6 or len(passwd)>20:
            response()
        
        elif not re.search('[a-z]', passwd):
            response()
        
        elif not re.search('[A-Z]', passwd):
            response()

        elif not re.search('[0-9]', passwd):
            response()
        
        elif not re.search('[!@#$%^&*()_-]', passwd):
            response()
        
        elif re.search('[ ]', passwd):
            print('Spaces are not allowed, try again.')
        
        else:
            print('Valid Password.')
            break

interaction()