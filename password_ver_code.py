# Program to determine whether a password meets defined parameters.
# Parameters : Between 5 and 16 char | No spaces | Must contain char & int | 
# Developer: Angela D. Tackett       CMIS102            28JUN22

#welcome
def welcome():
    print('\n\n      Xxxxxx Password xxxxX\n\n')

#prompt for input
def enter():
    while True:
        password = str(input('Enter what you want password to be: '))
        if len(password) > 5 and len(password) < 16:
            break   
        else:
            print('\nmust be between 6 and 15 characters\n')
    return password

#remove spaces
def rem_space(password):
    while True:
        if password.count(' ') == 0:
            print('\ngood job - no spaces found!')
            break
        elif password.count(' ') > 0:
            print('\nsorry - password may not contain spaces')
            def main():
                welcome()
                password = enter()
                password = rem_space(password)
                password = char_dig(password)
            main()
    return password


#character_digits check
def char_dig(password):
    while True:
        if password.isalpha():
            print(f'\npassword must contain at least one letter and one number')
            def main():
                welcome()
                password = enter()
                password = rem_space(password)
                password = char_dig(password)
            main()
        else:
            print(f'\n{password} falls within acceptable parameters.')
            break
    return password

            
def main():
    welcome()
    password = enter()
    password = rem_space(password)
    password = char_dig(password)
main()















    
