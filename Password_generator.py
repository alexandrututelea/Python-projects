import random
import string
def password_generator():
    password_list = []
    nr_characters = int(input("How many characters should your password have?(minimum 6): "))
    for char in range(nr_characters):
        if nr_characters >= 6:
            password_list.append(random.choice(string.ascii_letters + string.punctuation + string.digits))
        else:
            print("Invalid option for characters number!")
            break
    password = "".join(char for char in password_list)
    return password
password_generator()