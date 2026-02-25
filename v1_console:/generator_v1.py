import random  
import string  

def generate_password(length=12): 

  letters = string.ascii_letters  
  digits = string.digits         
  symbols = string.punctuation   

  all_chars = letters + digits + symbols 

  password = ''.join(random.choice(all_chars) for _ in range(length)) 

  return password  

user_length = int(input("Password length: ")) 
print("Your password:", generate_password(user_length))  
