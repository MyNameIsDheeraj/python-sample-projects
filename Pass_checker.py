import re

password = input("Enter your password \n")

while not password.strip():
    password = input ("Please enter password \n")

    if not password:
        print("Password canot be empty. Enter a valid password \n")

def special_char(passw):
    patter = r"[!@#$%^&*()_+={}[\]|:;'<>,.?/~\"]" 
    return bool(re.search(patter, passw))
    
def cap_char(passw):
    patter = r"[A-Z]"
    return bool(re.search(patter, passw))

def num_char(passw):
    patter = r"[0-9]"
    return bool(re.search(patter, passw))

if special_char(password) and cap_char(password) and num_char(password):
    print("Youre password is striong......!!!")

elif (special_char(password) and cap_char(password)) or (cap_char(password) and num_char(password)) or (num_char(password) and special_char(password)):
    print("Youre password is Moderate....!")

else:
    print("Pleas change youre password...its too weak")
