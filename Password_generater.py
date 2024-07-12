import random # we are importing the rendom library which is use to generate random values

def password_generator(): # we are creating a password_generator() function 
  
    try: # we use try block to handle exception (to stop unwanted termination of execution of program)     
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # upper case latters
        lower_letters = 'abcdefghijklmnopqrstuvwxyz' # lower case latters
        digits = '0123456789' # integer values
        punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`' # special characters
        characters = lower_letters + upper_letters + digits + punctuation  # we are combining all the charecters and store in the character variable
        
        length = int(input("Enter the desired length for the password greter then 5: "))
        
        if length > 5:
            password = ''.join(random.choice(characters) for _ in range(length))
            print("generated password is: ",password)
        else:
            print("Length should be a positive integer and grater then 5.")
    except:
        print("invalid")
        
password_generator()
