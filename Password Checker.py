import re

def response():
    print('Password must be atlease 6-20 characters long, contain uppercase, lowercase, a number and a symbol, try again.')


while True:
    passwd = input('Input a Password:')
    if len(passwd)<6 or len(passwd)>20:
        response()
        
    elif not re.search('[a-z]', passwd):
        response()
        
    elif not re.search('[A-Z]', passwd):
        response()
        
    elif not re.search('[_$@#-]', passwd):
        response()
        
    elif re.search('[ ]', passwd):
        print('Spaces are not allowed, try again.')
        
    else:
        print('Valid Password.')
        break

