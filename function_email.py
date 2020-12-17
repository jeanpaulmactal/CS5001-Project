def email():
    '''A function that checks if the email requirements of "@" and "." is included in the input
    '''

    email = ""

    while "@" and "." not in email:
        email = input("\nPlease enter a valid email address: ")
        email.lower().replace(" ", "_")

    return email