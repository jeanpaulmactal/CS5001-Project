def password():

    password = input("\nEnter your password: ")
    MINIMUM_LENGTH = 8
    
    while len(password) < MINIMUM_LENGTH or password.isalpha() == True or password.isdecimal() == True:
        '''Checks that the password length is at least 8 characters long and prompts the user to enter a new password
           with at least 8 characters if it is less
        '''

        if len(password) < MINIMUM_LENGTH and (password.isalpha() == False and password.isdecimal() == False):
            print("Your password must be at least 8 characters long")
        
        elif len(password) >= MINIMUM_LENGTH and (password.isalpha() == True or password.isdecimal() == True):
            print("Your password must be alphanumeric")

        elif len(password) < MINIMUM_LENGTH and password.isalpha() == True:
            print("Your password must be at least 8 characters long and alphanumeric - all alphabetical")
        
        elif len(password) < MINIMUM_LENGTH and password.isdecimal() == True:
            print("Your password must be at least 8 characters long and alphanumeric - all decimal")

        password = input("\nEnter a new password: ")

    return password