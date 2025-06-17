def is_strong_password(password):
    if (len(password) < 8):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_' for char in password):
        return False
    return True
    
print(is_strong_password("jdeb@"))
print(is_strong_password("jagrata@"))
print(is_strong_password("jagrataDeb6"))
print(is_strong_password("jagrataDeb6@"))