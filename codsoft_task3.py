import random
import string

def password_generator(leng,complexity):
    special= "@!#$%&*"
    if complexity=="easy":
        chars = string.ascii_lowercase + string.digits
    elif complexity == "medium":
        chars = string.ascii_lowercase + string.digits +special
    elif complexity =="hard":
        chars = string.ascii_letters + string.digits + special

    password= "".join(random.choice(chars) for i in range(leng))
    return password
    
password_len= int(input("Please enter the desired length of your password: "))
password_comp= input("Enter the desired complexity of the password as easy, medium or hard: ")

Password = password_generator(password_len,password_comp)
print("Your desired password is: ", Password)
