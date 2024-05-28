import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    return True

print(is_strong_password("Password123"))
print(is_strong_password("password123"))
print(is_strong_password("PASSWORD123"))
print(is_strong_password("Pass123"))    

